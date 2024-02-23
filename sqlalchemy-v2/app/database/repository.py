import uuid
from typing import Generic, TypeVar

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models

Model = TypeVar("Model", bound=models.Base)

class DatabaseRepository(Generic[Model]):
    """ Repository for database operations """
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session
    async def create(self, data: dict) -> Model:
        pass

    async def get(self, pk: uuid.UUID) -> Model | None:
        pass

    async def filter(self, *expression: BinaryExpression) -> list[Model]:
        pass