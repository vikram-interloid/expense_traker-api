
from app.repositories.report_repository import ReportRepository
from decimal import Decimal
from app.models.user import User
from app.schemas.report import MonthlyReportResponse,YearlyReportResponse







class ReportService:

    def __init__(
        self,
        repository: ReportRepository,
    ):
        self.repository = repository

    def get_total_income(
        self,
        current_user: User,
    ) -> Decimal:

        return self.repository.get_total_income(
            current_user.id,
        )
        
    def get_total_expense(
    self,
    current_user: User,
    ) -> Decimal:
        
        return self.repository.get_total_expense(
            current_user.id,
        )
        
    def get_balance(
    self,
    current_user: User,
    ) -> Decimal:
        total_income = self.repository.get_total_income(
            current_user.id,
        )
        total_expense = self.repository.get_total_expense(
        current_user.id,
        )
        return total_income - total_expense
    
    
    
    def get_monthly_report(
    self,
    current_user: User,
    year: int,
    month: int,
    ) -> MonthlyReportResponse:
        total_income = self.repository.get_total_income(
            user_id=current_user.id,
            year=year,
            month=month,
        )
        total_expense = self.repository.get_total_expense(
            user_id=current_user.id,
            year=year,
            month=month,
        )
        return MonthlyReportResponse(
            year=year,
            month=month,
            total_income=total_income,
            total_expense=total_expense,
            balance=total_income - total_expense,
        )
        
        
        
    def get_yearly_report(
        self,
        current_user: User,
        year: int,
    ) -> YearlyReportResponse:
        total_income = self.repository.get_total_income(
            user_id=current_user.id,
            year=year,
        )
        total_expense = self.repository.get_total_expense(
            user_id=current_user.id,
            year=year,
        )
        return YearlyReportResponse(
        year=year,
        total_income=total_income,
        total_expense=total_expense,
        balance=total_income - total_expense,
        )
        

        

    
    


    