from typing import List

from pydantic import BaseModel, constr

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


class AdRetrieveSchema(AdDetailSchema, AdCreateSchema):
    pass
    # comments = List
