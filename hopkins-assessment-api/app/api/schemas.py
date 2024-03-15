from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
"""
Assessor (pk, email, role, name) -> 101, tricia@maddiesplace.org, Superuser, Tricia Hughes
Role (pk, role_label, role_name) -> {101, SUPERUSER, Superuser}, {101, NURSE, Nurse}
Child (pk, name, birth_date, admission_date, discharge_date)
Domain (pk, domain_label, domain_name) -> {101, OPTIMAL, Optimal}, {102, MILD_DYSFUNCTION, Mild Dysfunction}
* AssessmentConfig(pk, domain_pk, assessment_item_code, assessment_item_name) ->
Assessment(pk, child_pk, assessor_pk, selected_assessment_item_code) -> {101, 101, }
"""

class Assessor(BaseModel):
    """ Assessor model """
    model_config = ConfigDict(from_attributes=True)
    pk: int
    email: str
    role: str
    name: str

class AssessorPayload(BaseModel):
    email: str
    role: str
    name: str

class Role(BaseModel):
    """ Role model """
    model_config = ConfigDict(from_attributes=True)
    pk: int
    role_label: str
    role_name: str

class RolePayload(BaseModel):
    role_label: str
    role_name: str

class Child(BaseModel):
    """ Child model """
    model_config = ConfigDict(from_attributes=True)
    pk: int
    name: str
    birth_date: datetime
    admission_date: datetime
    discharge_date: datetime

class ChildPayload(BaseModel):
    name: str
    birth_date: datetime
    admission_date: datetime
    discharge_date: datetime