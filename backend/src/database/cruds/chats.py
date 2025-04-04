from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from ..db_manager import DatabaseManager
from ..models import Chat

if TYPE_CHECKING:
    from . import CommonCRUD


class ChatsCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def add_chat(
        self,
        chat_id: int,
        topic: str,
        accounts_banned: int = 0,
    ) -> Chat:
        async with self.db.get_session() as session:
            new_chat = Chat(
                id=chat_id,
                topic=topic,
                accounts_banned=accounts_banned,
            )
            session.add(new_chat)
            await session.commit()
            await session.refresh(new_chat)
            return new_chat

    async def get_chat(self, chat_id: int) -> Optional[Chat]:
        async with self.db.get_session() as session:
            result = await session.execute(select(Chat).where(Chat.id == chat_id))
            return result.scalars().first()

    async def get_chats(self) -> List[Chat]:
        async with self.db.get_session() as session:
            chats = await session.execute(
                select(Chat).options(selectinload(Chat.topic))
            )
            return chats.scalars().all()
