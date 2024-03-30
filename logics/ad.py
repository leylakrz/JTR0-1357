from typing import Sequence

from sqlalchemy import Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models import User, Ad
from schemas.ad import AdCreateSchema, AdDetailSchema, AdListSchema
from schemas.user import CreatorSchema


async def ad_create(ad_info: AdCreateSchema, user: User, db: AsyncSession) -> Ad:
    new_obj = Ad(**ad_info.dict(), creator=user)
    db.add(new_obj)
    await db.commit()
    return new_obj


async def ad_list(db: AsyncSession) -> AdListSchema:
    query = select(Ad.id, Ad.title, User.id, User.email) \
        .join(User, Ad.creator_id == User.id)
    result = await db.execute(query)
    return convert_ads_to_dict(result.fetchall())


def convert_ads_to_dict(ads: Sequence[Row]) -> AdListSchema:
    return AdListSchema(data=[
        AdDetailSchema(id=ad_id, title=ad_title, creator=CreatorSchema(id=creator_id, email=creator_email))
        for ad_id, ad_title, creator_id, creator_email in ads
    ])
