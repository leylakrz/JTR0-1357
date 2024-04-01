from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

from logics.authentication.token import generate_access_token
from logics.utils import hash_password
from models import User
from schemas.user import UserLoginSchema


async def user_register(user_info: UserLoginSchema, db: AsyncSession) -> bool:
    # hash password
    hashed_password = hash_password(user_info.password)
    # create user if unique
    new_user = User(email=user_info.email, password=hashed_password)
    db.add(new_user)
    try:
        await db.commit()
    except IntegrityError:  # email is not unique
        await db.rollback()
        return False
    else:
        return True


async def user_login(user_info: UserLoginSchema, db: AsyncSession) -> Optional[dict]:
    # hash password
    hashed_password = hash_password(user_info.password)
    # retrieve user from db
    query = select(User).filter(User.email == user_info.email, User.password == hashed_password)
    result = await db.execute(query)
    user = result.scalar()
    if not user:
        return
    # generate token
    return {"access_token": generate_access_token(user.id)}


async def get_user_by_id(user_id: int, db: AsyncSession) -> Optional[User]:
    query = select(User) \
        .filter(User.id == user_id) \
        .options(load_only(User.id, User.email))
    result = await db.execute(query)
    return result.scalar()
