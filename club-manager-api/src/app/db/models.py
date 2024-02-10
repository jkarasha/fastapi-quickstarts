import uuid

from sqlalchemy import column, ForeignKey, Table, orm
from sqlalchemy.dialects.postgresql import UUID

class Base(orm.declarative_base()):
    """Base database model"""
    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

class Organization(Base):
    """Organization database model"""

    __tablename__ = "organization"

    name = orm.Mapped[str]
    description = orm.Mapped[str]
    street = orm.Mapped[str]
    city = orm.Mapped[str]
    state = orm.Mapped[str]
    zip = orm.Mapped[str]

class User(Base):
    """User database model"""

    __tablename__ = "user"

    username = orm.Mapped[str]
    email = orm.Mapped[str]
    password = orm.Mapped[str]