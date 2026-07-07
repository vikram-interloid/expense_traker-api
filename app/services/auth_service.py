
from datetime import datetime, timedelta, timezone

from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.exceptions.auth import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
)
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.repositories.auth_repository import AuthRepository
from app.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
)


class AuthService:
    def __init__(
        self, 
        repository: AuthRepository
    ):
        self.repository = repository

    def register(
        self,
        request: UserRegisterRequest,
    ) -> User:

        if self.repository.get_user_by_email(request.email):
            raise UserAlreadyExistsException()

        if self.repository.get_user_by_username(request.username):
            raise UserAlreadyExistsException()

        user = User(
            username=request.username,
            email=request.email,
            password_hash=hash_password(request.password),
        )

        return self.repository.create_user(user)

    def login(
        self,
        request: UserLoginRequest,
    ) -> TokenResponse:

        user = self.repository.get_user_by_email(request.email)

        if not user:
            raise InvalidCredentialsException()

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise InvalidCredentialsException()

        access_token = create_access_token(
            {"sub": str(user.id)}
        )

        refresh_token = create_refresh_token(
            {"sub": str(user.id)}
        )

        refresh = RefreshToken(
            token=refresh_token,
            user_id=user.id,
            expires_at=datetime.now(timezone.utc)
            + timedelta(
                days=settings.refresh_token_expire_days
            ),
        )

        self.repository.create_refresh_token(refresh)

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )



