import uuid
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class UserDB(UserSchema):
    id: uuid.UUID