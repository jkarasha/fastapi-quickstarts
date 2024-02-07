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