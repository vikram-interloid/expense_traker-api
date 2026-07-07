# from fastapi import APIRouter
# from sqlalchemy import text

# from app.core.redis import redis_client
# from app.db.session import SessionLocal

# router = APIRouter(prefix="/health", tags=["Health"])


# @router.get("/")
# def health():
#     return {"status": "ok"}


# @router.get("/db")
# def database_health():
#     db = SessionLocal()
#     try:
#         db.execute(text("SELECT 1"))
#         return {"database": "connected"}
#     finally:
#         db.close()


# @router.get("/redis")
# def redis_health():
#     redis_client.ping()
#     return {"redis": "connected"}


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.redis import redis_client
from app.db.session import get_db

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health():
    return {"status": "ok"}


@router.get("/db")
def database_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"database": "unavailable"},
        )


@router.get("/redis")
def redis_health():
    try:
        redis_client.ping()
        return {"redis": "connected"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"redis": "unavailable"},
        )