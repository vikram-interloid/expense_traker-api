from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models.user import User

from app.core.dependencies import get_auth_service,get_current_user,get_category_service
from app.schemas.auth import (
    TokenResponse,
    UserRegisterRequest,
    UserLoginRequest,
    UserResponse,
    RefreshTokenRequest,
    LogoutRequest,
    RegisterResponse,
    LoginResponse,
    RefreshResponse,
    MessageResponse
)
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)
oauth = APIRouter(
    prefix="/oauth"
)

@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: UserRegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    return service.register(request)



@router.post(
    "/login",
    response_model= LoginResponse,
    status_code=status.HTTP_200_OK,
)
def login(
    request: UserLoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    return service.login(
        email= request.email,
        password= request.password,
    )
    
@oauth.post(
    "/login",
    response_model= TokenResponse,
    status_code= status.HTTP_200_OK, 
    
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
):
    return service.login(
        email=form_data.username,
        password=form_data.password
    )

@router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
def me(
    current_user:User = Depends(get_current_user)
):
    return current_user

@router.post(
    "/refresh",
    response_model=RefreshResponse,
    status_code=status.HTTP_200_OK,
)
def refresh(
    request:RefreshTokenRequest,
    service: AuthService = Depends(get_auth_service),
):
    return service.refresh_access_token(
        request.refresh_token,
    )

@router.post(
    "/logout",
    response_model= MessageResponse,
    status_code=status.HTTP_200_OK,
)
def logout(
    request: LogoutRequest,
    service:AuthService=Depends(get_auth_service)
):
    service.logout(
        request.refresh_token
    )
    
    return {
        "message": "logout sucessful"
    }

