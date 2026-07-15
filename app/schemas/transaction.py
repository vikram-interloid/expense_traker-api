from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.models.category import CategoryType


class TransactionCreateRequest(BaseModel):
    amount: Decimal = Field(
        gt=0,
    )

    description: str | None = Field(
        default=None,
        max_length=255,
    )

    transaction_date: date

    category_id: int = Field(
        gt=0,
    )


class CategorySummary(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    name: str
    type: CategoryType


class TransactionResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    amount: Decimal
    description: str | None
    transaction_date: date
    category: CategorySummary
    user_id: int
    created_at: datetime


class CreateTransactionResponse(BaseModel):
    message: str
    data: TransactionResponse


class TransactionUpdateRequest(BaseModel):
    amount: Decimal = Field(
        gt=0,
    )

    description: str | None = Field(
        default=None,
        max_length=255,
    )

    transaction_date: date

    category_id: int = Field(
        gt=0,
    )


class PaginationResponse(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int


class TransactionListResponse(BaseModel):
    pagination: PaginationResponse
    data: list[TransactionResponse]
