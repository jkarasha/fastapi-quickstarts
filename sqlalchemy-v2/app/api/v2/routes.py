import uuid
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from app.api import models
from app.api.v2.dependencies import get_repository
from app.database import models as db_models
from app.database.repository import DatabaseRepository

router = APIRouter(prefix="/v2", tags=["v2"])

IngredientRepository = Annotated[
    DatabaseRepository[db_models.Ingredient],
    Depends(get_repository(db_models.Ingredient)),
]

PotionsRepository = Annotated[
    DatabaseRepository[db_models.Potion],
    Depends(get_repository(db_models.Potion)),

]

@router.post("/ingredients", status_code=status.HTTP_201_CREATED)
async def create_ingredient():
    pass

@router.get("/ingredients", status_code=status.HTTP_200_OK)
async def get_ingredients():
    pass

@router.get("/ingredients/{pk}", status_code=status.HTTP_200_OK)
async def get_ingredient(pk: uuid.UUID):
    pass

@router.put("/potions", status_code=status.HTTP_201_CREATED)
async def create_potion():
    pass

@router.get("/potions", status_code=status.HTTP_200_OK)
async def get_potions():
    pass

@router.get("/potions/{pk}", status_code=status.HTTP_200_OK)
async def get_potion(pk: uuid.UUID):
    pass

