from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from logics.authentication.authentication import authenticate
from logics.comment import comment_create
from resources.postgres.session import get_postgres_async_session as get_db
from schemas.comment import CommentCreateSchema, CommentDetailSchema

comment_router = APIRouter(tags=["comment"], prefix="/comment")


@comment_router.post("", response_model=CommentDetailSchema)
async def create_comment(body: CommentCreateSchema, db=Depends(get_db), user=Depends(authenticate)):
    result = await comment_create(body, user, db)
    if result:
        return result
    return JSONResponse(status_code=400, content={"detail": "Not allowed."})
