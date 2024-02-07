from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import org, users
from app.db import database, metadata, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

metadata.create_all(engine)

@app.get("/")
def index():
    return {"message": "Hello World!"} 

app.include_router(org.org_router, prefix="/orgs", tags=["org"])
app.include_router(users.user_router, prefix="/users", tags=["users"])