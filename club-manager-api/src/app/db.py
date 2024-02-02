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

DATABASE_URL = "sqlite:///./club-manager.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

org = Table(
    "organization",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("org_name", String(100)),
    Column("org_description", String(255)),
    Column("org_email", String(100)),
    Column("org_phone", String(15)),
    Column("org_website", String(100)),
    Column("org_street", String(100)),
    Column("org_city", String(50)),
    Column("org_state", String(50)),
    Column("org_zip", String(10)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

database = Database(DATABASE_URL)