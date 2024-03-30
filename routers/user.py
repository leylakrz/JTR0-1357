from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from logics.user import user_register, user_login
from resources.postgres.get_postgres_session import get_postgres_async_session as get_db
from schemas.user import UserLoginSchema

user_router = APIRouter(tags=["user"])


@user_router.post("/register")
async def register(body: UserLoginSchema, db=Depends(get_db)):
    if await user_register(body, db):
        return JSONResponse(status_code=200, content={"message": "Registered successfully."})
    return JSONResponse(status_code=400, content={"error": "Email exists."})


@user_router.post("/login")
async def login(body: UserLoginSchema, db=Depends(get_db)):
    token = await user_login(body, db)
    if token:
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=400, content={"error": "Wrong email or Password."})
