from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.db import close_db, init_db
from app.routers import api, pages

app = FastAPI(title="개인 건강관리 (실습)")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
async def startup():
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    await close_db()


app.include_router(pages.router)
app.include_router(api.router, prefix="/api", tags=["api"])
