from sqlalchemy import Column, String

from models.base import BaseModel


class User(BaseModel):
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
