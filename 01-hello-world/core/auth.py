from typing import Optional, MutableMapping, List, Union
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
from jose import jwt

from models.user import User
from core.config import settings
from core.security import verify_password

JWTPayloadMapping = MutableMapping[
    str,
    Union[str, datetime, List[str]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

def authenticate():
    pass

def create_access_token():
    pass

def _create_token():
    pass