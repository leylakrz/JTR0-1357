from typing import List, Optional

from pydantic import BaseModel, constr

from schemas.comment import CommentDetailSchema
from schemas.user import CreatorSchema


class AdCreateSchema(BaseModel):
    title: constr(max_length=100)
    description: str


class AdDetailSchema(BaseModel):
    id: int
    title: str
    creator: CreatorSchema


class AdListSchema(BaseModel):
    data: List[AdDetailSchema]


class AdRetrieveSchema(AdDetailSchema):
    description: str
    comments: List[CommentDetailSchema] = []


class AdUpdateSchema(BaseModel):
    title: Optional[constr(max_length=100)] = None
    description: Optional[str] = None
