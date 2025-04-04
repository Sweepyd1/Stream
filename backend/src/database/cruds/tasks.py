from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Numeric, and_, func, or_, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import false, true

from ..db_manager import DatabaseManager
from ..enums import BalanceChangeType
from ..errors.errors import TariffNotFoundError, TaskNotFoundError
from ..models import Tariff, Task, TaskProcessHistory, User

if TYPE_CHECKING:
    from . import CommonCRUD


class TasksCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def add_task(
        self,
        customer_id: int,
        text: str,
        topic_id: str,
        media: str,
        suspended: bool = False,
    ) -> Task:
        async with self.db.get_session() as session:
            new_task = Task(
                customer_id=customer_id,
                text=text,
                topic_id=topic_id,
                suspended=suspended,
                media=media,
            )
            session.add(new_task)
            await session.commit()
            await session.refresh(new_task)
            return new_task

    async def get_task(
        self, task_id: int, session: AsyncSession = None
    ) -> Optional[Task]:
        async with self.db.get_session(session) as session:
            result = await session.execute(
                select(Task)
                .where(Task.id == task_id)
                .options(
                    selectinload(Task.topic),
                    selectinload(Task.tariff).subqueryload(Tariff.abstract_tariff),
                )
            )
            return result.scalars().first()

    async def get_my_tasks(self, user_id: int) -> List[Task]:
        async with self.db.get_session() as session:
            tasks = await session.execute(
                select(Task)
                    .where(Task.customer_id == user_id)
                    .order_by(Task.created_at)
            )
            return tasks.scalars().all()

    async def get_processable_tasks_easy_but_slow(self) -> List[Task]:
        """We get all the tasks that can be performed.
        This function shows, in a simpler and easier to understand style,
        of how it can be done. But it's a lot slower than it would be
        than if we were doing it in SQL.

        Conditions:
        - Not paused
        - Daily message limit
        - Interval between
        - User's active rate

        Returns:
            List[Task]: A list of tasks that can be performed.
        """
        suitable_tasks = []

        async with self.db.get_session() as db:
            ##==> Берем задачи, которые не на паузе
            # И у которых подписка активна
            ############################
            q1 = await db.execute(
                select(Task)
                .where(
                    and_(
                        Task.suspended == false(),
                        and_(
                            Task.sub_expiration_date.isnot(None),
                            Task.sub_expiration_date > func.timezone("UTC", func.now()),
                        ),
                        and_(
                            Task.sub_purchase_date.isnot(None),
                            Task.sub_purchase_date < func.timezone("UTC", func.now()),
                        ),
                    )
                )
                .options(selectinload(Task.topic), selectinload(Task.tariff))
            )
            tasks = q1.scalars().all()

            for task in tasks:
                task: Task

                ##==> Получаем границы текущего дня
                # Относительно task.purchase_date
                ###############################################
                days_passed = int(
                    (datetime.now(timezone.utc) - task.sub_purchase_date).days
                )  # округляем в меньшую сторону
                start_current_day = task.sub_purchase_date + timedelta(
                    days=days_passed
                )  # Когда текущий день начался относительно task.purchase_date
                end_current_day = task.sub_purchase_date + timedelta(
                    days=days_passed + 1
                )  # Когда текущий день закончится относительно task.purchase_date

                ##==> Проверяем интервал между сообщениями
                #############################################
                last_sent_at = (
                    (
                        await db.execute(
                            select(func.max(TaskProcessHistory.sent_at))
                            .select_from(TaskProcessHistory)
                            .where(TaskProcessHistory.task_id == task.id)
                        )
                    )
                    .scalars()
                    .first()
                )

                if last_sent_at is not None:
                    if (
                        last_sent_at + timedelta(minutes=task.tariff.msgs_time_interval)
                    ) > datetime.now(timezone.utc):
                        print("Не прошла по интервалу")
                        continue  # Интервал между сообщениями еще не прошел

                ##==> Проверяем количество сообщений за сегодня
                ##################################################
                count_msgs = (
                    (
                        await db.execute(
                            select(func.count(TaskProcessHistory.id))
                            .select_from(TaskProcessHistory)
                            .where(
                                and_(
                                    TaskProcessHistory.task_id == task.id,
                                    TaskProcessHistory.sent_at >= start_current_day,
                                    TaskProcessHistory.sent_at < end_current_day,
                                )
                            )
                        )
                    )
                    .scalars()
                    .first()
                )

                if count_msgs >= task.tariff.msgs_per_day:
                    print("Не прошла по количеству сообщений за день")
                    continue  # Количество сообщений за текущий день превышает лимит

                suitable_tasks.append(task)

        return suitable_tasks

    async def get_processable_tasks_optimized(self, debug: bool = False) -> List[Task]:
        """We get all the tasks that can be performed.
        This function shows in a more optimized style,
        how this can be done using SQL.

        Conditions:
        - Not on pause
        - Daily message limit
        - Interval between
        - User's active rate

        Args:
            debug (bool, optional): Output logs for each task. Defaults to False.

        Returns:
            List[Task]: A list of tasks that can be performed.
        """
        async with self.db.get_session() as db:
            # Получаем текущее время в UTC
            now_utc = func.timezone("UTC", func.current_timestamp())

            # Подзапрос для получения времени последнего отправленного сообщения для каждой задачи
            subquery_last_sent = (
                select(
                    TaskProcessHistory.task_id,
                    func.max(TaskProcessHistory.sent_at).label("last_sent_at"),
                )
                .group_by(TaskProcessHistory.task_id)
                .subquery()
            )

            # Рассчитываем количество дней с момента покупки
            days_since_purchase = func.ceil(
                func.extract("epoch", now_utc - Task.sub_purchase_date) / 86400
            )

            # Рассчитываем day_start и day_end для каждой задачи
            day_start = Task.sub_purchase_date + (
                days_since_purchase * text("INTERVAL '1 day'")
            )
            day_end = day_start + text("INTERVAL '1 day'")

            # Подзапрос для подсчета количества сообщений, отправленных сегодня для каждой задачи
            subquery_msg_count = (
                select(
                    TaskProcessHistory.task_id,
                    func.count(TaskProcessHistory.id).label("msg_count"),
                )
                .join(Task, TaskProcessHistory.task_id == Task.id)
                .where(
                    TaskProcessHistory.sent_at >= day_start,
                    TaskProcessHistory.sent_at < day_end,
                )
                .group_by(TaskProcessHistory.task_id)
                .subquery()
            )

            # Псевдоним для Tariff.msgs_time_interval
            tariff_msgs_time_interval = Tariff.msgs_time_interval.label(
                "tariff_msgs_time_interval"
            )

            # Рассчитываем время с момента последней отправки сообщения для задачи (для проверки интервала)
            time_since_last_sent = (
                func.extract(
                    "epoch",
                    now_utc
                    - func.coalesce(
                        func.timezone("UTC", subquery_last_sent.c.last_sent_at),
                        Task.sub_purchase_date,
                    ),
                )
            ) / 60
            time_since_last_sent_label = time_since_last_sent.label(
                "time_since_last_sent_div"
            )

            # Основной запрос
            if debug:
                query_select = select(
                    Task,
                    day_start.label("day_start"),
                    day_end.label("day_end"),
                    time_since_last_sent.label("time_since_last_sent_div"),
                    tariff_msgs_time_interval,
                    now_utc,
                    subquery_last_sent.c.last_sent_at,
                    subquery_msg_count.c.msg_count,
                )
            else:
                query_select = select(Task)

            query = (
                query_select.outerjoin(
                    subquery_last_sent, Task.id == subquery_last_sent.c.task_id
                )
                .outerjoin(subquery_msg_count, Task.id == subquery_msg_count.c.task_id)
                .join(
                    Tariff,
                    and_(
                        Task.topic_id == Tariff.topic_id,
                        Task.abstract_tariff_id == Tariff.abstract_tariff_id,
                    ),
                )
                .where(
                    and_(
                        Task.suspended == false(),
                        Task.sub_expiration_date.isnot(None),
                        Task.sub_expiration_date > now_utc,
                        Task.sub_purchase_date.isnot(None),
                        Task.sub_purchase_date < now_utc,
                        # Проверяем интервал между сообщениями
                        or_(
                            subquery_last_sent.c.last_sent_at.is_(None),
                            time_since_last_sent_label >= Tariff.msgs_time_interval,
                        ),
                        # Проверяем количество сообщений в день
                        or_(
                            subquery_msg_count.c.msg_count.is_(None),
                            subquery_msg_count.c.msg_count < Tariff.msgs_per_day,
                        ),
                    )
                )
                .distinct()
                .options(
                    selectinload(Task.topic),
                    selectinload(Task.tariff).subqueryload(Tariff.topic),
                )
            )

            result = await db.execute(query)

            # Выводим результаты
            if debug:
                suitable_tasks = []

                for row in result.fetchall():
                    task = row[0]
                    day_start_val = row[1]
                    day_end_val = row[2]
                    time_since_last_sent_div = row[3]
                    tariff_interval = row[4]
                    now = row[5]
                    last_sent_at = row[6]
                    msg_count = row[7]
                    print(
                        f"Task ID: {task.id}, now: {now}, "
                        f"message_last_sent: {last_sent_at}, "
                        f"Time Since Last Sent DIVISION: {time_since_last_sent_div}, "
                        f"Tariff Interval: {tariff_interval}, "
                        f"Message Count: {msg_count}, "
                        f"Day Start: {day_start_val}, "
                        f"Day End: {day_end_val}"
                    )
                    suitable_tasks.append(task)

                return suitable_tasks
            else:
                return result.scalars().all()

    async def update_task_status(self, task_id: int, suspended: bool) -> Optional[Task]:
        task = await self.get_task(task_id)

        async with self.db.get_session() as session:
            task = await self.get_task(task_id=task_id, session=session)

            if task is None:
                return None

            task.suspended = suspended
            await session.commit()
            await session.refresh(task)
            return task

    async def update_task_autorenewal(
        self, task_id: int, enabled: bool
    ) -> Optional[Task]:
        async with self.db.get_session() as session:
            task = await self.get_task(task_id=task_id, session=session)

            if task is None:
                raise TaskNotFoundError(task_id=task_id)

            task.autorenewal = enabled
            await session.commit()
            await session.refresh(task)
            return task

    async def create_task_sub(
        self, task_id: int, tariff_id: int, count_months: int, with_pay: bool = False
    ) -> None:
        task = await self.get_task(task_id=task_id)

        if not task:
            return False

        async with self.db.get_session() as session:
            task = await self.get_task(task_id=task_id, session=session)

            if not task:
                raise TaskNotFoundError(task_id)

            tariff: Tariff = (
                await session.execute(select(Tariff).where(Tariff.id == tariff_id))
            ).scalar_one_or_none()

            if not tariff:
                raise TariffNotFoundError(tariff_id)

            task.abstract_tariff_id = tariff.abstract_tariff_id
            now = datetime.now(timezone.utc)
            task.sub_purchase_date = now
            task.sub_expiration_date = now + timedelta(days=31 * count_months)

            if with_pay:
                await self.common.users.change_user_balance(
                    user_id=task.customer_id,
                    operation_type=BalanceChangeType.PAY,
                    value=tariff.price_per_day * 31 * count_months,
                )

            await session.commit()

    async def extend_task_sub(
        self, task_id: int, count_months: int, with_pay: bool = False
    ) -> None:
        async with self.db.get_session() as session:
            task = await self.get_task(task_id=task_id, session=session)

            if not task:
                raise TaskNotFoundError(task_id)

            exp_date = task.sub_expiration_date
            task.sub_expiration_date = exp_date + timedelta(days=31 * count_months)

            if with_pay:
                await self.common.users.change_user_balance(
                    user_id=task.customer_id,
                    operation_type=BalanceChangeType.PAY,
                    value=task.tariff.price_per_day * 31 * count_months,
                )

            await session.commit()
            return True

    async def get_tasks_for_autorenewal(self) -> List[Task]:
        now = func.timezone("UTC", func.current_timestamp())

        async with self.db.get_session() as session:
            tasks = (
                await session.execute(
                    select(Task)
                    .join(User, User.id == Task.customer_id)
                    .join(
                        Tariff,
                        and_(
                            Tariff.abstract_tariff_id == Task.abstract_tariff_id,
                            Tariff.topic_id == Task.topic_id,
                            Tariff.disabled == false(),
                        ),
                    )
                    .where(
                        Task.autorenewal == true(),
                        Task.sub_expiration_date.isnot(None),
                        Task.sub_expiration_date < now,
                        Task.abstract_tariff_id.isnot(None),
                        User.balance >= Tariff.price_per_day * func.cast(31, Numeric),
                    )
                )
            ).scalars().all()

            return tasks
        
    async def delete_task(self, task_id: int):
        async with self.db.get_session() as session:
            result = await session.execute(select(Task).where(Task.id == task_id))
            task = result.scalars().first()

            if task:
                await session.delete(task)
                await session.commit()
            else:
                raise TaskNotFoundError(task_id)
