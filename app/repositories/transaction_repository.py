from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import date
from decimal import Decimal


from app.schemas .query_params import SortBy,SortOrder
from app.models import Transaction,Category
from app.models.category import CategoryType


class TransactionRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_category_by_id(
        self,
        category_id: int,
        user_id: int,
    ) -> Category | None:

        stmt = (
            select(Category)
            .where(
                Category.id == category_id,
                Category.user_id == user_id,
            )
        )

        return self.db.scalar(stmt)

    def create_transaction(
        self,
        transaction: Transaction,
    ) -> Transaction:

        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)

        return transaction
    
    def get_transactions_by_user(
        self,
        user_id: int,
        category_id: int | None = None,
        type: CategoryType | None = None,
        start_date:date |None = None,
        end_date: date | None = None,
        min_amount:Decimal | None = None,
        max_amount:Decimal | None =None,
        page:int =1,
        page_size: int =10,
        sort_by: SortBy = SortBy.TRANSACTION_DATE,
        sort_order: SortOrder = SortOrder.DESC,
        ) -> list[Transaction]:
        stmt = (
            select(Transaction)
            .join(Category)
            .where(
                Transaction.user_id == user_id,
            )
        )
        if category_id is not None:
            stmt = stmt.where(
                Transaction.category_id == category_id,
            )
        if type is not None:
            stmt = stmt.where(
                Category.type == type,
            )
        if start_date is not None:
            stmt = stmt.where(
                Transaction.transaction_date >= start_date,
            )
            
        if end_date is not None:
            stmt = stmt.where(
                Transaction.transaction_date <= end_date,
            )
        if min_amount is not None:
            stmt = stmt.where(
                Transaction.amount >= min_amount,
            )
        if max_amount is not None:
            stmt = stmt.where(
                Transaction.amount <= max_amount,
            )
        
        if sort_by == SortBy.AMOUNT:
            column = Transaction.amount
        else:
            column = Transaction.transaction_date
        if sort_order == SortOrder.ASC:
            stmt = stmt.order_by(column.asc())
        else:
            stmt = stmt.order_by(column.desc())
            
        offset = (page - 1) * page_size
        stmt = stmt.offset(offset).limit(page_size)
    
        return list(
        self.db.scalars(stmt).all()
        )
        
    
    
    
    def get_transaction_by_id(
    self,
    transaction_id: int,
    user_id: int,
    ) -> Transaction | None:
        stmt = (
            select(Transaction)
            .where(
            Transaction.id == transaction_id,
            Transaction.user_id == user_id,
        )
    )
        return self.db.scalar(stmt)
    
    def update_transaction(
    self,
    transaction: Transaction,
    ) -> Transaction:
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    
    def delete_transaction(
    self,
    transaction: Transaction,
    ) -> None:
        self.db.delete(transaction)
        self.db.commit()