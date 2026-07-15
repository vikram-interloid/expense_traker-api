
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
from app.models import User, RefreshToken
from app.repositories.auth_repository import AuthRepository
from app.schemas.auth import (
    TokenResponse,
    UserRegisterRequest,
    UserRegisterRequest,
    RegisterResponse,
    LoginResponse,
    RefreshResponse,
    MessageResponse

)




class AuthService:
    def __init__(self, repository: AuthRepository):
        self.repository = repository

    def register(
        self,
        request: UserRegisterRequest,
    ) -> RegisterResponse:

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

        user = self.repository.create_user(user)
        return RegisterResponse(
            message="User registered successfully",
            data=user,
        )

    def login(
        self,
        email:str,
        password:str,
    ) ->LoginResponse:
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
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": settings.access_token_expire_minutes * 60,
        }
        
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
            
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
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
    

    def refresh_access_token(
        self,
        refresh_token: str,
        ) -> RefreshResponse:
        db_token = self.repository.get_refresh_token(refresh_token)
        if db_token is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token",
            )
        try:
            payload = decode_token(refresh_token)
        except JWTError:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token",
            )
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token",
            )
        access_token = create_access_token(
            {"sub": str(user_id)}
        )
        
        return {
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": settings.access_token_expire_minutes * 60,
        }
        
        
    def logout(
        self,
        refresh_token:str,
    )-> MessageResponse:
        success = self.repository.revoke_refresh_token(
            refresh_token,
        )
        if not success:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token", 
            )
        return{
            "message":"logout successful"
        }
    
    
    
    
        
        
    
