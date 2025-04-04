from typing import TYPE_CHECKING, List

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.sql.expression import false, true

from ..db_manager import DatabaseManager
from ..models import AccountChat

if TYPE_CHECKING:
    from . import CommonCRUD


class AccountChatsCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def get_account_chats(
        self, account_id: int, without_bun: bool = False
    ) -> List[int]:
        async with self.db.get_session() as session:
            query = select(AccountChat.chat_id).where(
                AccountChat.account_id == account_id
            )

            if without_bun:
                query = query.where(AccountChat.banned == false()).where(
                    AccountChat.in_chat == true()
                )

            chats = await session.execute(query)
            return chats.scalars().all()

    async def set_account_chat_banned(
        self, account_id: int, chat_id: int, banned: bool = True
    ) -> None:
        async with self.db.get_session() as session:
            await session.execute(
                update(AccountChat)
                .where(AccountChat.account_id == account_id)
                .where(AccountChat.chat_id == chat_id)
                .values(banned=banned)
            )
            await session.commit()

    async def set_account_chat_in_chat(
        self, account_id: int, chat_id: int, in_chat: bool = True
    ) -> None:
        async with self.db.get_session() as session:
            await session.execute(
                update(AccountChat)
                .where(AccountChat.account_id == account_id)
                .where(AccountChat.chat_id == chat_id)
                .values(in_chat=in_chat)
            )
            await session.commit()
