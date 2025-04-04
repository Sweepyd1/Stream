from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional, Union
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from ...loader import cfg
from ..db_manager import DatabaseManager
from ..enums import BalanceChangeType
from ..errors.errors import PayNotFoundError
from ..models import PaymentHistory

if TYPE_CHECKING:
    from . import CommonCRUD


class PaymentHistoryCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def add_pay(
        self, user_id: int, amount: int, provider: str, currency: str = "USD"
    ) -> PaymentHistory:
        async with self.db.get_session() as session:
            new_pay = PaymentHistory(
                user_id=user_id,
                amount=amount,
                currency=currency,
                provider=provider,
                referral_percentage=cfg.bot.referral_percentage,
            )

            session.add(new_pay)
            await session.commit()
            await session.refresh(new_pay)
            return new_pay

    async def finalize_pay(self, pay_id: Union[UUID, str], with_pay: bool = True):
        """Accrues balance to the user as well as his referral.
        Records the transaction in the payment history

        Args:
            pay_id (Union[UUID, str]): payment identificator
            with_pay (bool, optional): To refill the user's balance or not. Defaults to True.
        """
        async with self.db.get_session() as session:
            pay: Optional[PaymentHistory] = await self.get_pay(
                pay_id=pay_id, with_user=True, session=session
            )

            if not pay:
                raise PayNotFoundError(pay_id)

            if pay.payed_at:
                return  # Pay already finalized

            if with_pay:
                ##==> Начисляем баланс пользователю
                await self.common.users.change_user_balance(
                    user_id=pay.user_id,
                    operation_type=BalanceChangeType.PLUS,
                    value=pay.amount,
                    session=session
                )

                ##==> начисляем бонус рефереру нашего пользователя
                if pay.user.referrer_id:
                    await self.common.users.change_user_balance(
                        user_id=pay.user.referrer_id,
                        operation_type=BalanceChangeType.PLUS,
                        value=pay.amount * cfg.bot.referral_percentage,
                        session=session
                    )

            pay.payed_at = datetime.now(timezone.utc)
            await session.commit()

    async def get_pay(
        self,
        pay_id: Union[UUID, str],
        with_user: bool = False,
        session: AsyncSession = None,
    ) -> Optional[PaymentHistory]:
        query = select(PaymentHistory).where(PaymentHistory.id == pay_id)

        if with_user:
            query = query.options(selectinload(PaymentHistory.user))

        async with self.db.get_session(session) as session:
            result = await session.execute(query)
            return result.scalars().first()

    async def get_user_pays(self, user_id: int) -> List[PaymentHistory]:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(PaymentHistory).where(PaymentHistory.user_id == user_id)
            )
            return result.scalars().all()

    async def get_pays(self) -> List[PaymentHistory]:
        async with self.db.get_session() as session:
            result = await session.execute(select(PaymentHistory))
            return result.scalars().all()
