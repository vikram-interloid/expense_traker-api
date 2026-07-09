

from pydantic import BaseModel, ConfigDict, Field

from app.models.category import CategoryType

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
