import logging

from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    """App settings."""

    project_name: str = "club-manager-api"
    debug: bool = False
    environment: str = "local"

    # Database
    database_url: str = "sqlite:///C:\\Dev\\Python\\fastapi-demos\\club-manager-api\\club-manager.db"


settings = Settings()