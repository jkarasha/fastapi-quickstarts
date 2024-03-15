from datetime import datetime
from sqlalchemy import Column, ForeignKey, Table, orm, Integer

"""
Assessor (pk, email, role, name) -> 101, tricia@maddiesplace.org, Superuser, Tricia Hughes
Role (pk, role_label, role_name) -> {101, SUPERUSER, Superuser}, {101, NURSE, Nurse}
Child (pk, name, birth_date, admission_date, discharge_date)
Domain (pk, domain_label, domain_name) -> {101, OPTIMAL, Optimal}, {102, MILD_DYSFUNCTION, Mild Dysfunction}
* AssessmentConfig(pk, domain_pk, assessment_item_code, assessment_item_name) ->
Assessment(pk, child_pk, assessor_pk, selected_assessment_item_code) -> {101, 101, }
"""
class Base(orm.DeclarativeBase):
    """ Base declarative class for all models """
    pk: orm.Mapped[int] = orm.mapped_column(primary_key=True,index=True)
    date_updated: orm.Mapped[datetime] = orm.mapped_column(default=datetime.now)
    date_created: orm.Mapped[datetime] = orm.mapped_column(default=datetime.now)

class Assessor(Base):
    """ Assessor model """
    __tablename__ = "assessor"
    email: orm.Mapped[str]
    role: orm.Mapped[str]
    name: orm.Mapped[str]

class Role(Base):
    """ Role model """
    __tablename__ = "role"
    role_label: orm.Mapped[str]
    role_name: orm.Mapped[str]


class Domain(Base): 
    """ Domain model """
    __tablename__ = "domain"
    domain_label: orm.Mapped[str]
    domain_name: orm.Mapped[str]

class AssessmentItem(Base):
    """ AssessmentConfig model """
    __tablename__ = "assessment_item"
    domain_pk: orm.Mapped[int]
    assessment_item_code: orm.Mapped[str]
    assessment_item_name: orm.Mapped[str]

child_assessment_item_association = Table(
    "child_assessment_item",
    Base.metadata,
    Column("child_id", Integer, ForeignKey("child.pk")),
    Column("assessment_item_id", Integer, ForeignKey("assessment_item.pk")),
    Column("assessor_id", Integer, ForeignKey("assessor.pk")),
)

class Child(Base):
    """ Child model """
    __tablename__ = "child"
    name: orm.Mapped[str]
    birth_date: orm.Mapped[datetime]
    admission_date: orm.Mapped[datetime]
    discharge_date: orm.Mapped[datetime]
    assessments: orm.Mapped[list[AssessmentItem]] = orm.relationship(
        secondary=child_assessment_item_association,
        backref="child",
        lazy="selectin")