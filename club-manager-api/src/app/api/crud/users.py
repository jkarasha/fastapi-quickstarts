from app.db import user, database
from app.api.models.users import UserSchema

async def post(payload: UserSchema):
    query = user.insert().values(username=payload.username, email=payload.email, password=payload.password)
    return await database.execute(query=query)

async def get(id: int):
    query = user.select().where(id == user.c.id)
    return await database.fetch_one(query=query)

async def get_all():
    query = user.select()
    return await database.fetch_all(query=query)

async def put(id: int, payload: UserSchema):
    query = user.update().where(id == user.c.id).values(username=payload.username, email=payload.email, password=payload.password)
    return await database.execute(query=query)

async def delete(id: int):
    query = user.delete().where(id == user.c.id)
    return await database.execute(query=query)

