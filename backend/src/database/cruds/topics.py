from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.future import select

from ..db_manager import DatabaseManager
from ..models import Topic

if TYPE_CHECKING:
    from . import CommonCRUD


class TopicsCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def add_topic(self, name: str) -> Topic:
        async with self.db.get_session() as session:
            new_topic = Topic(name=name)
            session.add(new_topic)
            await session.commit()
            await session.refresh(new_topic)
            return new_topic

    async def get_topic(self, topic_id: int) -> Optional[Topic]:
        async with self.db.get_session() as session:
            result = await session.execute(select(Topic).where(Topic.id == topic_id))
            return result.scalars().first()

    async def get_topics(self) -> List[Topic]:
        async with self.db.get_session() as session:
            users = await session.execute(select(Topic))
            return users.scalars().all()
