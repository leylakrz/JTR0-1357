from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from logics.ad import ad_create, ad_list, ad_delete, ad_update, ad_retrieve
from logics.authentication.authentication import authenticate
from resources.postgres.session import get_postgres_async_session as get_db
from schemas.ad import AdCreateSchema, AdListSchema, AdRetrieveSchema, AdDetailSchema, AdUpdateSchema

ad_router = APIRouter(tags=["ad"], prefix="/ad")


@ad_router.post("", response_model=AdDetailSchema)
async def create_ad(body: AdCreateSchema, user=Depends(authenticate), db=Depends(get_db)):
    return await ad_create(body, user, db)


@ad_router.get("", response_model=AdListSchema)
async def list_ads(db=Depends(get_db)):
    result = await ad_list(db)
    return {"data": result}


@ad_router.get("/{ad_id}", response_model=AdRetrieveSchema)
async def retrieve_ad(ad_id: int, db=Depends(get_db)):
    result = await ad_retrieve(ad_id, db)
    if result:
        return result
    raise HTTPException(status_code=404)


@ad_router.patch("/{ad_id}", response_model=AdRetrieveSchema)
async def update_ad(ad_id: int, body: AdUpdateSchema, user=Depends(authenticate), db=Depends(get_db)):
    result = await ad_update(ad_id, body, user, db)
    if result:
        return result
    raise HTTPException(status_code=404)


@ad_router.delete("/{ad_id}")
async def delete_ad(ad_id: int, user=Depends(authenticate), db=Depends(get_db)):
    result = await ad_delete(ad_id, user, db)
    if result:
        return JSONResponse(status_code=200, content={"message": "Deleted successfully."})
    raise HTTPException(status_code=404)
