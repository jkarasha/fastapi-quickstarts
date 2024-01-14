from fastapi import FastAPI
from app.api import ping, notes
from app.db import database, engine, metadata

metadata.create_all(engine)

newapp = FastAPI()

@newapp.get("/")
def root():
    return {"message": "Hello World"}


@newapp.on_event("startup")
async def startup():
    await database.connect()

@newapp.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    

newapp.include_router(ping.router)
newapp.include_router(notes.router, prefix="/notes", tags=["notes"])
