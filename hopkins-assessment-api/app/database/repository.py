from typing import Generic, TypeVar

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models

Model = TypeVar("Model", bound=models.Base)

class DatabaseRepository(Generic[Model]):

    """ Repository for database operations"""

    def __init__(self, model: type(Model), session: AsyncSession) -> None:
        self.model = model
        self.session = session
    
    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh()
        return instance

    async def get(self, pk: int) -> Model | None:
        return await self.session.get(self.model, pk)

    async def filter(self, *expressions: BinaryExpression) -> list(Model):
        #
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)

        return list(await self.session.scalars(query))

