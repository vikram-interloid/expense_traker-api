from fastapi import APIRouter, Depends, status, Query
from datetime import date
from decimal import Decimal
from app.schemas.query_params import SortBy,SortOrder

from app.core.dependencies import (
    get_current_user,
    get_transaction_service,
)
from app.models import User
from app. models.category import CategoryType
from app.schemas.transaction import (
    TransactionCreateRequest,
    TransactionResponse,
    TransactionUpdateRequest,
    CreateTransactionResponse,
    TransactionListResponse
)
from app.services.transaction_service import TransactionService

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post(
    "",
    response_model= CreateTransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_transaction(
    request: TransactionCreateRequest,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(
        get_transaction_service,
    ),
):
    return service.create_transaction(
        request,
        current_user,
    )


@router.get(
    "",
    response_model= TransactionListResponse,
    status_code=status.HTTP_200_OK,
)
def get_transactions(
    category_id: int | None = Query(default=None),
    type: CategoryType |None = Query(default=None),
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    min_amount: Decimal | None = Query(default=None),
    max_amount: Decimal | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    sort_by: SortBy = Query(default=SortBy.TRANSACTION_DATE),
    sort_order: SortOrder =  Query(default=SortOrder.DESC),
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(
        get_transaction_service,
    ),
):
    return service.get_transactions(
        current_user=current_user,
        category_id=category_id,
        type=type,
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
        page =page,
        page_size = page_size,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    
@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse,
    status_code=status.HTTP_200_OK,
)
def get_transaction_by_id(
    transaction_id: int,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(
        get_transaction_service,
    ),
):
    return service.get_transaction_by_id(
        transaction_id,
        current_user,
    )                                                                    
@router.put(
    "/{transaction_id}",
    response_model=TransactionResponse,
    status_code=status.HTTP_200_OK,
)
def update_transaction(
    transaction_id: int,
    request: TransactionUpdateRequest,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(
        get_transaction_service,
    ),
):
    return service.update_transaction(
        transaction_id,
        request,
        current_user,
    )
    
    
@router.delete(
    "/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_transaction(
    transaction_id: int,
    current_user: User = Depends(get_current_user),
    service: TransactionService = Depends(
        get_transaction_service,
    ),
):
    service.delete_transaction(
        transaction_id,
        current_user,
    )   