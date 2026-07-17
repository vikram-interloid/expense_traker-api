from app.core.dependencies import Session
from decimal import Decimal
from sqlalchemy import func,select,extract
from app.models import Transaction,Category
from app.models.category import CategoryType
from uuid import UUID



class ReportRepository:
    def __init__(
        self,
        db:Session
    ):
        self.db =db
    def get_total_income(
        self,
        user_id: UUID,
        year: int | None = None,
        month: int | None = None,
    ) ->Decimal:
        
        stmt =(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0,
                )
            )
            .join(Category)
            .where(
                Transaction.user_id == user_id,
                Category.type == CategoryType.INCOME, 
            )
        )
        if year is not None:
            stmt = stmt.where(
            extract(
                "year",
                Transaction.transaction_date,
                )
                == year
            )
        if month is not None:
            stmt =stmt.where(
                extract(
                    "month",
                    Transaction.transaction_date
                )
                == month
            )
        return self.db.scalar(stmt)
    
    
    
    
    def get_total_expense(
    self,
    user_id: UUID,
    year: int | None = None,
    month: int | None = None,
    ) -> Decimal:
        stmt = (
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0,
                )
            )
            .join(Category)
            .where(
                Transaction.user_id == user_id,
                Category.type == CategoryType.EXPENSE,
            )
        )
        if year is not None:
            stmt = stmt.where(
            extract(
                "year",
                Transaction.transaction_date,
                )
                == year
            )
        if month is not None:
            stmt = stmt.where(
            extract(
                "month",
                Transaction.transaction_date,
                )
                == month
            )
        return self.db.scalar(stmt)
    
    
    
    
    
    
    
    
    

    


