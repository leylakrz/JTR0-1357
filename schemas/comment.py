from pydantic import BaseModel

from schemas.user import CreatorSchema


class CommentCreateSchema(BaseModel):
    text: str
    ad_id: int


class CommentDetailSchema(BaseModel):
    id: int
    text: str
    creator: CreatorSchema
