from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = "sqlite:///C:\\Dev\\Python\\fastapi-demos\\club-manager-api\\club-manager.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

org = Table(
    "organization",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), unique=True, index=True),
    Column("description", String(255)),
    Column("street", String(100)),
    Column("city", String(50)),
    Column("state", String(50)),
    Column("zip", String(10))
)

database = Database(DATABASE_URL)