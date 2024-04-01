from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_async_engine(settings.POSTGRES_ASYNC_TEST_URL, echo=True, future=True)


async def get_postgres_test_async_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


engine_sync = create_engine(settings.POSTGRES_TEST_URL)


def get_postgres_test_sync_session():
    sync_session = sessionmaker(engine_sync, expire_on_commit=False)()
    try:
        yield sync_session
    finally:
        sync_session.close()
