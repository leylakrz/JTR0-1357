from typing import Optional

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, load_only

from models import User, Ad, Comment
from schemas.ad import AdCreateSchema, AdUpdateSchema


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


async def ad_update(ad_id, ad_info: AdUpdateSchema, user: User, db: AsyncSession) -> Optional[Ad]:
    obj = await ad_retrieve_for_update(ad_id, user.id, db)
    if not obj:
        return
    for key, value in ad_info.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    await db.commit()
    return obj


async def ad_retrieve_for_update(ad_id, creator_id, db) -> Optional[Ad]:
    query = select(Ad) \
        .options(
        load_only(Ad.title, Ad.description),
        selectinload(Ad.creator).load_only(User.id, User.email),
        selectinload(Ad.comments).load_only(Comment.id, Comment.text)
        .options(selectinload(Comment.creator).load_only(User.id, User.email))
    ) \
        .where(Ad.id == ad_id, Ad.creator_id == creator_id)
    result = await db.execute(query)
    return result.scalar()


async def ad_delete(ad_id, user: User, db: AsyncSession) -> bool:
    query = delete(Ad).where(Ad.id == ad_id, Ad.creator_id == user.id)
    result = await db.execute(query)
    if result.rowcount == 0:
        return False
    else:
        await db.commit()
        return True
