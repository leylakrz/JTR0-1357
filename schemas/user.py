from pydantic import BaseModel, constr, EmailStr, Field


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(max_length=50)
    password: constr(max_length=50, min_length=4)
