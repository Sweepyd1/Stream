from typing import TYPE_CHECKING, List

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from ..db_manager import DatabaseManager
from ..models import AbstractTariff, Tariff

if TYPE_CHECKING:
    from . import CommonCRUD


class TariffsCRUD:
    db: DatabaseManager

    def __init__(self, db: DatabaseManager, common_crud: "CommonCRUD") -> None:
        self.db = db
        self.common = common_crud

    async def get_abstract_tariffs(self) -> List[AbstractTariff]:
        async with self.db.get_session() as session:
            tasks = await session.execute(select(AbstractTariff))
            return tasks.scalars().all()

    async def get_tariffs(
        self, can_buy: bool = False, topic_id: int = None
    ) -> List[Tariff]:
        async with self.db.get_session() as session:
            query = select(Tariff).options(
                selectinload(Tariff.topic), selectinload(Tariff.abstract_tariff)
            )

            if can_buy:
                query = query.where(Tariff.disabled == False)

            if topic_id:
                query = query.where(Tariff.topic_id == topic_id)

            tasks = await session.execute(query)
            return tasks.scalars().all()

    async def get_tariff(self, tariff_id: int) -> Tariff:
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Tariff)
                .where(Tariff.id == tariff_id)
                .options(
                    selectinload(Tariff.topic), selectinload(Tariff.abstract_tariff)
                )
            )
            return result.scalars().first()
