from fastapi import FastAPI

from .database import engine
from .init_db import Base
from fapi.advert.router import router as auth_router
from fapi.advert.router import advert_router

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def create_app():
    app = FastAPI(
        debug=True,
        docs_url="/v1/docs",
        title="FastAPI SService Documentation",
    )

    @app.on_event("startup")
    async def startup_event():
        await create_tables()
        
    app.include_router(advert_router)
    return app
