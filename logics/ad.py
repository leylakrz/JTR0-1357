from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Ad
from schemas.ad import AdCreateSchema


async def ad_create(ad_info: AdCreateSchema, user: User, db: AsyncSession) -> Ad:
    new_obj = Ad(**ad_info.dict(), creator=user)
    db.add(new_obj)
    await db.commit()
    return new_obj
