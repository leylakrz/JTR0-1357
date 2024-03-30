from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, load_only
from sqlmodel import select

from models import User, Ad, Comment
from schemas.ad import AdCreateSchema, AdListSchema


async def ad_create(ad_info: AdCreateSchema, user: User, db: AsyncSession) -> Ad:
    new_obj = Ad(**ad_info.dict(), creator=user)
    db.add(new_obj)
    await db.commit()
    return new_obj


async def ad_list(db: AsyncSession) -> list[Ad]:
    query = (
        select(Ad)
        .options(
            load_only(Ad.id, Ad.title),
            selectinload(Ad.creator).load_only(User.id, User.email)
        )
    )
    result = await db.execute(query)
    return result.scalars().all()


async def ad_retrieve(ad_id: int, db: AsyncSession) -> Optional[Ad]:
    query = select(Ad) \
        .options(
        load_only(Ad.title, Ad.description),
        selectinload(Ad.creator).load_only(User.id, User.email),
        selectinload(Ad.comments).load_only(Comment.id, Comment.text)
        .options(selectinload(Comment.creator).load_only(User.id, User.email))
    ) \
        .where(Ad.id == ad_id)
    result = await db.execute(query)
    return result.scalar()
