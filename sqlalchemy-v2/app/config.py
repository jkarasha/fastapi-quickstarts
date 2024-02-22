import logging

from pydantic import BaseSettings

logging.basicConfig(level=logging.INFO)

class Settings(BaseSettings):
    """ App Settings"""
    project_name: str = "SQLAlchemy v2 with FastAPI"
    debug: bool = False
    environment: str = "development"
    database_url: str = ""

settings = Settings()

