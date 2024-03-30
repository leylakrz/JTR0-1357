from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Ad, Comment
from schemas.comment import CommentCreateSchema


async def comment_create(ad_info: CommentCreateSchema, user: User, db: AsyncSession) -> Optional[Ad]:
    new_obj = Comment(**ad_info.dict(), creator=user)
    db.add(new_obj)
    try:
        await db.commit()
    except IntegrityError:  # either the ad_id does not exist or user has already created a comment for this ad.
        return
    else:
        return new_obj
