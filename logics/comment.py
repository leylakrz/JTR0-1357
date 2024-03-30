from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, load_only
from sqlmodel import select

from models import User, Ad, Comment
from schemas.ad import AdListSchema
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


async def comment_list(db: AsyncSession) -> AdListSchema:
    query = (
        select(Comment)
        .options(
            load_only(Comment.text),
            selectinload(Comment.creator).load_only(User.id, User.email)
        )
    )
    result = await db.execute(query)
    return result.scalars().all()
