from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

import crud
import schemas
from api import deps

from core.auth import (
    authenticate,
    create_access_token
)
from models.user import User

router = APIRouter()

@router.post("/login")
def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Get JWT access token with data from OAuth2 form.
    """
    user = authenticate(
        email=form_data.username,
        password=form_data.password,
        db=db
    )
    #
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    #
    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "bearer"
    }

@router.post("/me", response_model=schemas.user.User)
def read_users_me(current_user: User = Depends(deps.get_current_user)):
    """
    Get current user.
    """
    return current_user

@router.post("/signup", response_model=schemas.user.User, status_code=status.HTTP_201_CREATED)
def create_user_signup(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.user.UserCreate
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    #
    user = crud.user.create(db, obj_in=user_in)
    return user
