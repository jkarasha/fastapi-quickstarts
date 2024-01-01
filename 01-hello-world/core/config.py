import pathlib

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, EmailStr, validator
from typing import List, Union

ROOT = pathlib.Path(__file__).parent.parent

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQL_ALCHEMY_DATABASE_URI: str = "sqlite:///./recipes.db"
    FIRST_SUPERUSER: EmailStr = "admin@recipeapi.com"

    class Config:
        case_sensitive = True

settings = Settings()
