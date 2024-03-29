from fastapi import FastAPI

from app.api import notes, ping
from app.db import engine, database, metadata
    
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.ping_router)
app.include_router(notes.notes_router, prefix="/notes", tags=["notes"])