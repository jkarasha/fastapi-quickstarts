import uuid

from pydantic import BaseModel, ConfigDict

class Organization(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    
    pk: uuid.UUID
    name: str
    description: str
    street: str
    city: str
    state: str
    zip: str