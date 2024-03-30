from fastapi import FastAPI

from routers import user_router, ad_router, comment_router

app = FastAPI(title="JTR0-1357")
app.include_router(user_router, prefix="/api")
app.include_router(ad_router, prefix="/api")
app.include_router(comment_router, prefix="/api")
