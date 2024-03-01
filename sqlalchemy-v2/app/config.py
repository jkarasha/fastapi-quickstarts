import os
import logging

from pydantic_settings import BaseSettings


logging.basicConfig(level=logging.INFO)

class Settings(BaseSettings):
    """ App Settings"""
    project_name: str = "The apothecary API"
    debug: bool = False
    environment: str = "development"
    basedir: str = os.path.abspath(os.path.dirname(__file__))
    database_url: str = "sqlite+aiosqlite:///" + os.path.join(basedir, "apothecary.db")

settings = Settings()

