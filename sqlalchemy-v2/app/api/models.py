import uuid

from pydantic import BaseModel, ConfigDict, Field

class Ingredient(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    pk: uuid.UUID
    name: str

class IngredientPayload(BaseModel):

    name: str = Field(min_length=1, max_length=128)


class Potion(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)

    pk: uuid.UUID
    name: str
    ingredients: list[Ingredient]

class PotionPayload(BaseModel):
    
    name: str = Field(min_length=1, max_length=128)
    ingredients: list[uuid.UUID] = Field(min_length=1)
