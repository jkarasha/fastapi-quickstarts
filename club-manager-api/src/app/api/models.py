from pydantic import BaseModel

class OrgSchema(BaseModel):
    name: str
    description: str
    street: str
    city: str
    state: str
    zip: str

class OrgDB(OrgSchema):
    id: int
