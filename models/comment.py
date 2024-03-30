from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import BaseDBModel


class Comment(BaseDBModel):
    text = Column(Text, nullable=False)
    creator_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    ad_id = Column(Integer, ForeignKey("ad.id"), nullable=False)

    creator = relationship("User", back_populates="comments")
    ad = relationship("Ad", back_populates="comments")
