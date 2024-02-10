import uuid
from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    pk: uuid.UUID
    username: str
    email: str
    password: str
