from typing import List

from pydantic import BaseModel, constr

from schemas.user import CreatorSchema


class AdCreateSchema(BaseModel):
    title: constr(max_length=100)
    description: str


class AdRetrieveSchema(AdCreateSchema):
    id: int
    creator: CreatorSchema


class AdListSchema(BaseModel):
    data: List[AdRetrieveSchema]
