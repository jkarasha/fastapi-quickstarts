import uuid
from typing import Generic, TypeVar, List, Optional

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import models

Model = TypeVar("Model", bound=models.Base)

class DatabaseRepository(Generic[Model]):
    """Repository for database operations."""
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, data: dict) -> Model:
        """Create a new record."""
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
    
    async def get(self, pk: uuid.UUID) -> Model | None:
        """Get a record by ID."""
        return await self.session.get(self.model, pk)
    
    async def filter(self, *expressions: BinaryExpression) -> List[Model]:
        """Filter records by expressions."""
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)
        return list(await self.session.scalars(query))