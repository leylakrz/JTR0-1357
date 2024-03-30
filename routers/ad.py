from fastapi import APIRouter, Depends

from logics.ad import ad_create
from logics.authentication.authentication import authenticate
from resources.postgres.get_postgres_session import get_postgres_async_session as get_db
from schemas.ad import AdCreateSchema, AdRetrieveSchema

ad_router = APIRouter(tags=["ad"], prefix="/ad")


@ad_router.post("", response_model=AdRetrieveSchema)
async def create_ad(body: AdCreateSchema, db=Depends(get_db), user=Depends(authenticate)):
    result = await ad_create(body, user, db)
    return result


@ad_router.get("")
async def list_ads(db=Depends(get_db)):
    pass


@ad_router.get("/{ad_id}")
async def retrieve_ad(ad_id: int, db=Depends(get_db)):
    pass
