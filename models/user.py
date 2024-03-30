from sqlalchemy import Column, String

from models.base import BaseDBModel


class User(BaseDBModel):
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
