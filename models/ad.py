from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import BaseDBModel


class Ad(BaseDBModel):
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    creator_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    creator = relationship("User", back_populates="ads")
    comments = relationship("Comment")
