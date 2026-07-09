

from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.health import router as health_router
from app.core.config import settings
from app.api.v1.category import router as category_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)



app.include_router(health_router)
app.include_router(auth_router)
app.include_router(category_router)