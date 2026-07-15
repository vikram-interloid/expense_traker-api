

from pydantic import BaseModel, ConfigDict, Field

from app.models.category import CategoryType
from datetime import datetime
class CategoryCreateRequest(BaseModel):
    name: str = Field(
        min_length=2, 
        max_length=50
    )
    type: CategoryType
class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    type: CategoryType
    user_id: int
    created_at: datetime
    updated_at : datetime
class CreateCategoryResponse(BaseModel):
    message: str
    data: CategoryResponse
class GetCategoryResponse(BaseModel):
    data: CategoryResponse
class CategoryUpdateRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
    )
    type: CategoryType  
class UpdateCategoryResponse(BaseModel):
    message: str
    data: CategoryResponse    
class CategoryListResponse(BaseModel):
    data: list[CategoryResponse]