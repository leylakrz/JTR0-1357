from .ad import Ad
from .base import Base
from .comment import Comment
from .user import User

table_names = [User.__tablename__, Ad.__tablename__, Comment.__tablename__]
table_names_str = ", ".join([f"\"{t}\"" for t in table_names])
