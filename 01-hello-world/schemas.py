from pydantic import BaseModel, HttpUrl
from typing import Sequence

class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl

class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl

class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]

class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int

class RecipeUpdate(RecipeBase):
    id: int

class RecipeUpdateRestricted(BaseModel):
    id: int
    label: str

class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

class RecipeInDB(RecipeInDBBase):
    pass