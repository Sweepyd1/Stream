from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from ..db_manager import DatabaseManager
from ..models import Task, TaskProcessHistory

if TYPE_CHECKING:
    from . import CommonCRUD


class TaskProcessHistoryCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def add_history(
        self,
        account_id: int,
        chat_id: int,
        message_id: int,
        task_id: int,
    ) -> TaskProcessHistory:
        async with self.db.get_session() as session:
            new_entry = TaskProcessHistory(
                account_id=account_id,
                chat_id=chat_id,
                message_id=message_id,
                task_id=task_id,
            )
            session.add(new_entry)
            await session.commit()
            await session.refresh(new_entry)
            return new_entry

    async def get_task_history(self, task_id: int) -> List[TaskProcessHistory]:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(TaskProcessHistory)
               .where(TaskProcessHistory.task_id == task_id)
               .order_by(TaskProcessHistory.sent_at)
            )
            return result.scalars().all()

    async def get_last_sent_message_for_dialog(
        self, chat_id: int
    ) -> TaskProcessHistory:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(TaskProcessHistory)
                .where(TaskProcessHistory.chat_id == chat_id)
                .order_by(TaskProcessHistory.sent_at.desc())
                .limit(1)
            )
            return result.scalars().first()

    async def get_last_sent_message_by_account_for_task_and_dialog(
        self, task_id: int, account_id: int, chat_id: int
    ) -> TaskProcessHistory:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(TaskProcessHistory)
                .where(TaskProcessHistory.task_id == task_id)
                .where(TaskProcessHistory.account_id == account_id)
                .where(TaskProcessHistory.chat_id == chat_id)
                .order_by(TaskProcessHistory.sent_at.desc())
                .limit(1)
            )
            return result.scalars().first()

    async def get_account_last_sent_time(self, account_id: int) -> Optional[datetime]:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(TaskProcessHistory.sent_at)
                .where(TaskProcessHistory.account_id == account_id)
                .order_by(TaskProcessHistory.sent_at.desc())
                .limit(1)
            )
            return result.scalar()

    async def get_sent_count_today_by_account(self, account_id: int) -> int:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(func.count(TaskProcessHistory.id))
                .where(
                    TaskProcessHistory.sent_at
                    >= datetime.now(timezone.utc).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                )
                .where(TaskProcessHistory.account_id == account_id)
            )
            return result.scalar()

    async def get_count_completed_for_task(self, task_id: int) -> int:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(func.count(TaskProcessHistory.id)).where(
                    TaskProcessHistory.task_id == task_id
                )
            )
            return result.scalar()

    async def get_tasks_history_for_period_for_user(
        self, user_id: int, from_: datetime, to: datetime, topic_id: int = None
    ) -> List[TaskProcessHistory]:
        async with self.db.get_session() as session:
            query = (
                select(TaskProcessHistory)
                .join(Task, Task.id == TaskProcessHistory.task_id)
                .where(Task.customer_id == user_id)
                .where(TaskProcessHistory.sent_at >= from_)
                .where(TaskProcessHistory.sent_at <= to)
                .options(selectinload(TaskProcessHistory.task))
            )

            if topic_id:
                query = query.where(Task.topic_id == topic_id)

            result = await session.execute(query)
            return result.scalars().all()
