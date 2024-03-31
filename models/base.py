from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr

from logics.utils import camel_to_snake

Base = declarative_base()


class BaseDBModel(Base):
    @declared_attr
    def __tablename__(cls):
        return camel_to_snake(cls.__name__)

    id = Column(Integer, primary_key=True)

    __abstract__ = True
