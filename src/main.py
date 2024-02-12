from fastapi import FastAPI
from auth.schemas import UserCreate,UserRead
from auth.base_config import auth_backend
from auth.base_config import fastapi_users
from fastapi.staticfiles import StaticFiles

from operations.router import router as operation_router
from tasks.router import router as tasks_router
from pages.router import router as pages_router
from chat.router import router as router_chat
from fastapi_cache import FastAPICache

from redis import asyncio as aioredis
from fastapi_cache.backends.redis import RedisBackend


app = FastAPI(
    title='Trading app'
)

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(operation_router)
app.include_router(tasks_router)
app.include_router(pages_router)
app.include_router(router_chat)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")