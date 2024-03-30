from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, load_only
from sqlmodel import select

from models import User, Ad
from schemas.ad import AdCreateSchema, AdListSchema


async def ad_create(ad_info: AdCreateSchema, user: User, db: AsyncSession) -> Ad:
    new_obj = Ad(**ad_info.dict(), creator=user)
    db.add(new_obj)
    await db.commit()
    return new_obj


async def ad_list(db: AsyncSession) -> AdListSchema:
    query = (
        select(Ad)
        .options(
            load_only(Ad.id, Ad.title),
            selectinload(Ad.creator).load_only(User.id, User.email)
        )
    )
    result = await db.execute(query)
    return result.scalars().all()
