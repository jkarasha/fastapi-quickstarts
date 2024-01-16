from fastapi import APIRouter, HTTPException, status
from typing import List
from app.api import crud
from app.api.models import NoteDB, NoteSchema

notes_router = APIRouter()


@notes_router.post("/", response_model=NoteDB, status_code=status.HTTP_201_CREATED)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

@notes_router.get("/{id}/", response_model=NoteDB)
async def read_note(id: int):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@notes_router.get("/", response_model=List[NoteDB])
async def read_all_notes():
    return await crud.get_all()

@notes_router.put("/{id}/", response_model=NoteDB)
async def update_note(id: int, payload: NoteSchema):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    #
    note_id = await crud.put(id, payload)
    #
    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    #
    return response_object

@notes_router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    await crud.delete(id)

    return note