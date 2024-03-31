from fastapi import APIRouter, Depends, HTTPException

from logics.ad import ad_create, ad_list, ad_retrieve
from logics.authentication.authentication import authenticate
from resources.postgres.session import get_postgres_async_session as get_db
from schemas.ad import AdCreateSchema, AdDetailSchema, AdListSchema

ad_router = APIRouter(tags=["ad"], prefix="/ad")


@ad_router.post("", response_model=AdDetailSchema)
async def create_ad(body: AdCreateSchema, db=Depends(get_db), user=Depends(authenticate)):
    return await ad_create(body, user, db)


@ad_router.get("", response_model=AdListSchema)
async def list_ads(db=Depends(get_db)):
    result = await ad_list(db)
    return {"data": result}


@ad_router.get("/{ad_id}")
async def retrieve_ad(ad_id: int, db=Depends(get_db)):
    result = await ad_retrieve(ad_id, db)
    if result:
        return result
    raise HTTPException(status_code=404)
