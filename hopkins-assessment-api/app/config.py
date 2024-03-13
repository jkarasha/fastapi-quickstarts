import os
import logging

from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)

class Settings(BaseSettings):
    """ Application settings"""
    project_name: str = "Maddie's Place Hopkins Assessment App"
    debug: bool = False
    environment: str = "Development"
    baseDir: str = os.path.abspath(os.path.dirname(__file__))
    database_url = f"sqlite+aoolite:///{os.path.join(baseDir, "maddies-place.db")}"

settings = Settings()