from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field
class UserRegisterRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: EmailStr
    created_at: datetime  
class RegisterResponse(BaseModel):
    message: str
    data : UserResponse
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str
class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
class RefreshTokenRequest(BaseModel):
    refresh_token: str
class RefreshResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
class LogoutRequest(BaseModel):
    refresh_token: str
class MessageResponse(BaseModel):
    message: str
    
class ErrorResponse(BaseModel):
    detail: str

    