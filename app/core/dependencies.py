from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.db.session import get_db
from app.repositories.auth_repository import AuthRepository
from app.services.auth_service import AuthService

from app.repositories.transaction_repository import TransactionRepository
from app.services.transaction_service import TransactionService

from app.repositories.category_repository import CategoryRepository
from app.services.category_service import CategoryService

from app.repositories.report_repository import ReportRepository
from app.services.report_service import ReportService

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/oauth/login",
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

def get_category_service(
    db: Session = Depends(get_db),
) -> CategoryService:

    repository = CategoryRepository(db)

    return CategoryService(repository)

def get_transaction_service(
    db: Session = Depends(get_db),
) -> TransactionService:

    repository = TransactionRepository(db)

    return TransactionService(repository)

def get_report_repository(
    db: Session = Depends(get_db),
) -> ReportRepository:

    return ReportRepository(
        db,
    )

def get_report_service(
    repository: ReportRepository = Depends(
        get_report_repository,
    ),
) -> ReportService:

    return ReportService(
        repository,
    )






    