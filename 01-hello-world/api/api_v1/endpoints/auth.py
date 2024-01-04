from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

import crud, schemas
from api import deps

#add import from core
from models.user import User

router = APIRouter()

@router.post("/login")
def login():
    pass

@router.post("/me", response_model=schemas.User)
def read_users_me():
    pass

@router.post("/signup", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user_signup():
    pass
