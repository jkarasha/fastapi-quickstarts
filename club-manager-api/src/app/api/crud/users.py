from app.db import user, database
from app.api.models.users import UserSchema

async def post(payload: UserSchema):
    query = user.insert().values(username=payload.username, email=payload.email, password=payload.password)
    return await database.execute(query=query)