
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction import TransactionCreateRequest,TransactionUpdateRequest

from fastapi import HTTPException, status
from app.models import User, Transaction
from decimal import Decimal,ROUND_HALF_UP
from app.schemas.query_params import SortBy,SortOrder
from uuid import UUID

from app.models.category import CategoryType
from datetime import date
from math import ceil


class TransactionService:

    def __init__(
        self,
        repository: TransactionRepository,
    ):
        self.repository = repository

    def create_transaction(
        self,
        request: TransactionCreateRequest,
        current_user: User,
    ) -> Transaction:

        category = self.repository.get_category_by_id(
            request.category_id,
            current_user.id,
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        transaction = Transaction(
            amount=request.amount.quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP,  
            ),
            description=request.description,
            transaction_date=request.transaction_date,
            category_id=request.category_id,
            user_id=current_user.id,
        )

        transaction = self.repository.create_transaction(
            transaction,
        )
        return {
            "message": "transaction created successfully",
            "data": transaction,
        }
        
        
    def get_transactions(
    self,
    current_user: User,
    category_id: UUID | None = None,
    type: CategoryType | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    min_amount: Decimal | None = None,
    max_amount: Decimal | None = None,
    page:int =1,
    page_size:int =10,
    sort_by: SortBy = SortBy.TRANSACTION_DATE,
    sort_order: SortOrder = SortOrder.DESC,
    
    ):
        transactions,total_records = self.repository.get_transactions_by_user(
            user_id=current_user.id,
            category_id=category_id,
            type=type,
            start_date=start_date,
            end_date=end_date,
            min_amount=min_amount,
            max_amount=max_amount,
            page =page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order =sort_order,
        )
        return {
            "data": transactions,
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total_records": total_records,
                "total_pages": ceil(total_records / page_size),
            },
        }
        
        
    def get_transaction_by_id(
    self,
    transaction_id: UUID,
    current_user: User,
    ) -> Transaction:
        transaction = self.repository.get_transaction_by_id(
            transaction_id,
            current_user.id,
        )
        if transaction is None:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )

        return transaction
    
    def update_transaction(
    self,
    transaction_id: UUID,
    request: TransactionUpdateRequest,
    current_user: User,
    ) -> Transaction:
        transaction = self.repository.get_transaction_by_id(
            transaction_id,
            current_user.id,
        )
        if transaction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction not found",
            )
        category = self.repository.get_category_by_id(
            request.category_id,
            current_user.id,
        )
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )
        transaction.amount = request.amount.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
            
        )
        transaction.description = request.description
        transaction.transaction_date = request.transaction_date
        transaction.category_id = request.category_id
        return self.repository.update_transaction(
        transaction,
    )
        
        
    def delete_transaction(
    self,
    transaction_id: UUID,
    current_user: User,
    ) -> None:

        transaction = self.repository.get_transaction_by_id(
            transaction_id,
            current_user.id,
        )

        if transaction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction not found",
            )
        self.repository.delete_transaction(
        transaction,
        )
    
