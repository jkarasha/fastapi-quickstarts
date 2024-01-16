from fastapi import APIRouter

ping_router = APIRouter()


@ping_router.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}