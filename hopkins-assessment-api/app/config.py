import os
import logging

from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)

class Settings(BaseSettings):
    """ Application settings"""
    project_name: str = "Maddie's Place Hopkins Assessment App"
    debug: bool = False
    environment: str = "Development"
    base_dir: str = os.path.abspath(os.path.dirname(__file__))
    database_url: str = "sqlite+aiosqlite:///" + os.path.join(base_dir, "maddies-place.db")

settings = Settings()