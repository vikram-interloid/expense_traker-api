from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class CategoryCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    type: CategoryType


class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    type: CategoryType
    user_id: int
