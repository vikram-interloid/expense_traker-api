from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.db.session import get_db
from app.repositories.auth_repository import AuthRepository
from app.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def get_auth_service(
    db: Session = Depends(get_db),
) -> AuthService:
    repository = AuthRepository(db)
    return AuthService(repository)

def get_current_user(
    token:str =Depends(oauth2_scheme),
    service:AuthService =Depends(get_auth_service)
):
    return service.get_current_user(token)

    