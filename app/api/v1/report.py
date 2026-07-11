from fastapi import APIRouter, Depends, status,Query

from app.core.dependencies import (
    get_current_user,
    get_report_service,
)
from app.models.user import User
from app.schemas.report import TotalIncomeResponse,TotalExpenseResponse,BalanceResponse,MonthlyReportResponse,YearlyReportResponse
from app.services.report_service import ReportService



router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)

@router.get(
    "/total-income",
    response_model=TotalIncomeResponse,
    status_code=status.HTTP_200_OK,
)
def get_total_income(
    current_user: User = Depends(get_current_user),
    service: ReportService = Depends(
        get_report_service,
    ),
):
    total = service.get_total_income(
        current_user,
    )

    return TotalIncomeResponse(
        total_income=total,
    )
    
    
@router.get(
    "/total-expense",
    response_model=TotalExpenseResponse,
    status_code=status.HTTP_200_OK,
)
def get_total_expense(
    current_user: User = Depends(get_current_user),
    service: ReportService = Depends(get_report_service),
):
    total = service.get_total_expense(
        current_user,
    )

    return TotalExpenseResponse(
        total_expense=total,
    )
    
@router.get(
    "/balance",
    response_model=BalanceResponse,
    status_code=status.HTTP_200_OK,
)
def get_balance(
    current_user: User = Depends(get_current_user),
    service: ReportService = Depends(get_report_service),
):
    balance = service.get_balance(
        current_user,
    )

    return BalanceResponse(
        balance=balance,
    )
    
    
@router.get(
    "/monthly",
    response_model=MonthlyReportResponse,
    status_code=status.HTTP_200_OK,
)
def get_monthly_report(
    year: int = Query(..., ge=2000),
    month: int = Query(..., ge=1, le=12),
    current_user: User = Depends(get_current_user),
    service: ReportService = Depends(get_report_service),
):
    return service.get_monthly_report(
        current_user=current_user,
        year=year,
        month=month,
    )
    
    
@router.get(
    "/yearly",
    response_model=YearlyReportResponse,
    status_code=status.HTTP_200_OK,
)
def get_yearly_report(
    year: int = Query(..., ge=2000),
    current_user: User = Depends(get_current_user),
    service: ReportService = Depends(get_report_service),
):
    return service.get_yearly_report(
        current_user=current_user,
        year=year,
    )
    
    
    