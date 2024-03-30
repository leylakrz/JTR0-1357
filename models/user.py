from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import BaseDBModel


class User(BaseDBModel):
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(64), nullable=False)

    ads = relationship("Ad")
    comments = relationship("Comment")
