from fastapi import FastAPI

from app.api.v1.auth import router as auth_router, oauth as oauth_router
from app.api.v1.health import router as health_router
from app.core.config import settings
from app.api.v1.category import router as category_router
from app.api.v1.category import router as category_router
from app.api.v1.report import router as report_router


from app.api.v1.transaction import (
    router as transaction_router,
)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

API_PREFIX = "/api/v1"

app.include_router(health_router, prefix=API_PREFIX)
app.include_router(auth_router, prefix=API_PREFIX )
app.include_router(category_router, prefix=API_PREFIX )
app.include_router(transaction_router, prefix=API_PREFIX)
app.include_router(report_router, prefix=API_PREFIX)
app.include_router(oauth_router, prefix=API_PREFIX)


