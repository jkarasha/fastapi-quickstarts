from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from app.config import settings

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """ Get a new database session"""
    engine = create_async_engine(settings.database_url)
    factory = async_sessionmaker(bind=engine)
    #
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError:
            await session.rollback()
            raise

