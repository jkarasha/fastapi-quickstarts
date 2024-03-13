from sqlalchemy import Column, ForeignKey, Table, orm, Integer
class Base(orm.DeclarativeBase):
    """ Base declarative class for all models """
    pk: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        index=True,
    )