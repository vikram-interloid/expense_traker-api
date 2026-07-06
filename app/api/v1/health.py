from fastapi import APIRouter
from sqlalchemy import text

from app.core.redis import redis_client
from app.db.session import SessionLocal

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health():
    return {"status": "ok"}


@router.get("/db")
def database_health():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        return {"database": "connected"}
    finally:
        db.close()


@router.get("/redis")
def redis_health():
    redis_client.ping()
    return {"redis": "connected"}