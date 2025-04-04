from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional

from loguru import logger
from sqlalchemy import func, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from ..db_manager import DatabaseManager
from ..enums import BalanceChangeType
from ..errors.errors import InsufficientFundsError, UserNotFoundError
from ..models import User

if TYPE_CHECKING:
    from . import CommonCRUD


class UsersCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def add_user(self, user_id: int, referrer_id: int = None, balance=0) -> User:
        async with self.db.get_session() as session:
            existing_user = await session.execute(
                select(User).where(User.id == user_id)
            )
            existing_user = existing_user.scalar()

            if existing_user:
                existing_user.updated_at = datetime.utcnow()
                await session.commit()
                return existing_user

            new_user = User(id=user_id, referrer_id=referrer_id, balance=balance)
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def get_user(
        self, user_id: int, session: AsyncSession = None
    ) -> Optional[User]:
        async with self.db.get_session(session) as s:
            result = await s.execute(select(User).where(User.id == user_id))
            return result.scalars().first()

    async def get_users(self) -> List[User]:
        async with self.db.get_session() as session:
            users = await session.execute(select(User))
            return users.scalars().all()

    async def get_count_users(self) -> int:
        async with self.db.get_session() as session:
            count = await session.scalar(select(func.count()).select_from(User))
            return count

    async def get_my_referrals(
        self, user_id: int, with_payment_history: bool = False
    ) -> List[User]:
        async with self.db.get_session() as session:
            query = select(User).where(User.referrer_id == user_id)

            if with_payment_history:
                query = query.options(selectinload(User.payment_history))

            users = await session.execute(query)
            return users.scalars().all()

    async def change_user_balance(
        self,
        user_id: int,
        operation_type: BalanceChangeType,
        value: Decimal,
        session: AsyncSession = None,
    ):
        async with self.db.get_session(session) as session:
            user = await self.get_user(user_id, session)

            if not user:
                raise UserNotFoundError(user_id)

            query = update(User).where(User.id == user_id)

            logger.debug(f"{operation_type}")

            if operation_type == BalanceChangeType.PLUS:
                query = query.values(balance=User.balance + value)
            elif operation_type == BalanceChangeType.MINUS:
                query = query.values(balance=User.balance - value)
            elif operation_type == BalanceChangeType.EQUATE:
                query = query.values(balance=value)
            elif operation_type == BalanceChangeType.PAY:
                if user.balance < value:
                    raise InsufficientFundsError(balance=user.balance, amount=value)
                query = query.values(balance=User.balance - value)
            else:
                raise ValueError(f'Unknown balance change type "{operation_type}"')

            await session.execute(query)
            await session.commit()
            return True

    async def set_mailing_notices_status(
        self, account_id: int, status: bool = True
    ) -> None:
        async with self.db.get_session() as session:
            await session.execute(
                update(User).where(User.id == account_id).values(mailing_notices=status)
            )
            await session.commit()

    async def set_referral_notices_status(
        self, account_id: int, status: bool = True
    ) -> None:
        async with self.db.get_session() as session:
            await session.execute(
                update(User)
                .where(User.id == account_id)
                .values(referral_notices=status)
            )
            await session.commit()

    async def set_news_notices_status(
        self, account_id: int, status: bool = True
    ) -> None:
        async with self.db.get_session() as session:
            await session.execute(
                update(User).where(User.id == account_id).values(news_notices=status)
            )
            await session.commit()

    async def set_balance_notices_status(
        self, account_id: int, status: bool = True
    ) -> None:
        async with self.db.get_session() as session:
            await session.execute(
                update(User).where(User.id == account_id).values(balance_notices=status)
            )
            await session.commit()
