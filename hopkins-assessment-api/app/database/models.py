from sqlalchemy import Column, ForeignKey, Table, orm, Integer
class Base(orm.DeclarativeBase):
    """ Base declarative class for all models """
    pk: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        index=True,
    )

### TODO: Build out the MP Hopkins Assessment App Model
"""
Assessor (pk, email, role, name) -> 101, tricia@maddiesplace.org, Superuser, Tricia Hughes
Role (pk, role_label, role_name) -> {101, SUPERUSER, Superuser}, {101, NURSE, Nurse}
Child (pk, name, birth_date, admission_date, discharge_date)
Domain (pk, domain_label, domain_name) -> {101, OPTIMAL, Optimal}, {102, MILD_DYSFUNCTION, Mild Dysfunction}
* AssessmentConfig(pk, domain_pk, assessment_item_code, assessment_item_name) ->
Assessment(pk, child_pk, assessor_pk, selected_assessment_item_code) -> {101, 101, }
"""