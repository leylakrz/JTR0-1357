from datetime import datetime

import jwt
from fastapi import HTTPException, Depends, Header
from jwt import DecodeError
from sqlalchemy.ext.asyncio import AsyncSession

from exceptions import AuthenticationFailed
from logics.user import get_user_by_id
from models import User
from resources.postgres.get_postgres_session import get_postgres_async_session as get_db
from settings import settings


async def authenticate(token: str = Header(None), db: AsyncSession = Depends(get_db)):
    try:
        return await validate_jwt(token, db)
    except AuthenticationFailed:
        raise HTTPException(status_code=403)


async def validate_jwt(token: str, db: AsyncSession) -> User:
    payload = jwt_decode(token)
    check_token_expiration(payload['exp'])
    return await get_user_by_id(payload['uid'], db)


def jwt_decode(token: str) -> dict:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except DecodeError:
        raise AuthenticationFailed


async def check_and_get_user(user_id: int, db: AsyncSession) -> User:
    user_obj = await get_user_by_id(user_id, db)
    if user_obj:
        return user_obj
    raise AuthenticationFailed


def check_token_expiration(expiration_timestamp: int) -> None:
    if datetime.now().timestamp() > expiration_timestamp:
        raise AuthenticationFailed
