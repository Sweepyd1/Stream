from typing import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self, database_url):
        self.engine = create_async_engine(database_url, echo=False)
        self.AsyncSession = sessionmaker(
            bind=self.engine, expire_on_commit=False, class_=AsyncSession
        )

    @asynccontextmanager
    async def get_session(self, existing_session: AsyncSession = None) -> AsyncIterator[AsyncSession]:
        if existing_session is None:
            async with self.AsyncSession() as session:
                try:
                    yield session
                except Exception:
                    await session.rollback()
                    raise
                finally:
                    await session.close()
        else:
            yield existing_session
            

Base = declarative_base()
