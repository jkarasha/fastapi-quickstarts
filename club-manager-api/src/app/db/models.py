import uuid
from sqlalchemy import String, orm

class Base(orm.DeclarativeBase):
    """Base database model"""
    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

class Organization(Base):
    """Organization database model"""

    __tablename__ = "organization"

    name = orm.Mapped[str] = orm.mapped_column(String(255), index=True, unique=True)
    description = orm.Mapped[str] = orm.mapped_column(String(255))
    street = orm.Mapped[str] = orm.mapped_column(String(100))
    city = orm.Mapped[str] = orm.mapped_column(String(50))
    state = orm.Mapped[str] = orm.mapped_column(String(50))
    zip = orm.Mapped[str] = orm.mapped_column(String(10))

class User(Base):
    """User database model"""

    __tablename__ = "user"

    username = orm.Mapped[str] = orm.mapped_column(String(50), index=True, unique=True)
    email = orm.Mapped[str] = orm.mapped_column(String(50), index=True, unique=True)
    password = orm.Mapped[str] = orm.mapped_column(String(50))
    