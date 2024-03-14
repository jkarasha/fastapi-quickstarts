from datetime import datetime
from sqlalchemy import Column, ForeignKey, Table, orm, Integer
class Base(orm.DeclarativeBase):
    """ Base declarative class for all models """
    pk: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        index=True,
    )
    date_updated: orm.Mapped[datetime] = orm.mapped_column(default=datetime.now)
    date_created: orm.Mapped[datetime] = orm.mapped_column(default=datetime.now)

class Ingredient(Base):
    """ Ingredient model """
    __tablename__ = "ingredient"
    name: orm.Mapped[str]

potion_ingredient_association = Table(
    "potion_ingredient",
    Base.metadata,
    Column("potion_id", Integer, ForeignKey("potion.pk")),
    Column("ingredient_id", Integer, ForeignKey("ingredient.pk")),
)

class Potion(Base):
    """ Potion model """
    __tablename__ = "potion"

    name: orm.Mapped[str]
    ingredients: orm.Mapped[list[Ingredient]] = orm.relationship(
        secondary=potion_ingredient_association,
        backref="potions",
        lazy="selectin",
    )
    