
from jose import JWTError    
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException ,status

from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
    decode_token
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
    def __init__(self, repository: AuthRepository):
        self.repository = repository

    def register(
        self,
        request: UserRegisterRequest,
    ) -> User:

        if self.repository.get_user_by_email(request.email):
            raise HTTPException(
                status_code=409,
                detail="email_already_exists"
            )

        if self.repository.get_user_by_username(request.username):
            raise HTTPException(
                status_code=409,
                detail="username_already_exists"
            )

        user = User(
            username=request.username,
            email=request.email,
            password_hash=hash_password(request.password),
        )

        return self.repository.create_user(user)

    def login(
        self,
        # request: UserLoginRequest,
        email:str,
        password:str,
    ) -> TokenResponse:
        user = self.repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )
    
    
 
        

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

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
        
    def get_current_user(
    self,
    token: str,
    ) -> User:

        try:
            payload = decode_token(token)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )
        user = self.repository.get_user_by_id(int(user_id))
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )
        return user
    
    
    
    
        
        
    
