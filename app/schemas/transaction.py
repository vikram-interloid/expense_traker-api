from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field




class TransactionCreateRequest(BaseModel):
    amount: Decimal = Field(gt=0)
    description: str | None = Field(
        default=None,
        max_length=255,
    )
    transaction_date: date
    category_id: int


class TransactionResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    amount: Decimal
    description: str | None
    transaction_date: date
    category_id: int
    user_id: int
    created_at: datetime

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