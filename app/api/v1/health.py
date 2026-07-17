
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

# from app.core.redis import redis_client
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health():
    return {"status": "ok"}

@router.get("/db")
def database_health(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        )

# @router.get("/redis")
# def redis_health():
#     try:
#         redis_client.ping()
#         return {"redis": "connected"}
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
#             detail={"redis": "unavailable"},
#         )

