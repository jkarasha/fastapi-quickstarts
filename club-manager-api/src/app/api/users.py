from fastapi import APIRouter, HTTPException, status
from app.api.crud import users as crud
from app.api.models.users import UserSchema, UserDB

user_router = APIRouter()

@user_router.post("/", response_model=UserDB, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserSchema):
    user_id = await crud.post(payload)

    response_object = {
        "id": user_id,
        "username": payload.username,
        "email": payload.email,
        "password": payload.password
    }

    return response_object

@user_router.get("/{id}/", response_model=UserDB)
async def read_user(id: int):
    user = await crud.get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with given id not found")
    return user

@user_router.get("/", response_model=list[UserDB])
async def read_all_users():
    return await crud.get_all()

@user_router.put("/{id}/", response_model=UserDB)
async def update_user(id: int, payload: UserSchema):
    user = await crud.get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with given id not found")
    user_id = await crud.put(id, payload)

    response_object = {
        "id": user_id,
        "username": payload.username,
        "email": payload.email,
        "password": payload.password
    }

    return response_object

@user_router.delete("/{id}/", response_model=UserDB)
async def delete_user(id: int):
    user = await crud.get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with given id not found")
    await crud.delete(id)
    return user