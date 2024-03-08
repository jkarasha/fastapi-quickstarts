from typing import Generic, TypeVar

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models

# Create a generic type variable called Model that is bound to the models.Base class
# This will only allow us to use this class with subclasses of models.Base
Model = TypeVar("Model", bound=models.Base)

class DatabaseRepository(Generic[Model]):
    """ Repository for database operations """

    # Initialize the repository with the type of model passed in and the session
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    # Create a new instance of the model with the data passed inSS
    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: int) -> Model | None:
        return await self.session.get(self.model, pk)

    async def filter(self, *expressions: BinaryExpression) -> list[Model]:
        #
        print(f"expressions: {expressions}, model: {self.model}")
        #
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)
        #
        print(f"query: {query}")
        #
        return list(await self.session.scalars(query))