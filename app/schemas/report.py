from decimal import Decimal

from pydantic import BaseModel
class TotalIncomeResponse(BaseModel):
    total_income: Decimal
class TotalExpenseResponse(BaseModel):
    total_expense: Decimal
class BalanceResponse(BaseModel):
    balance: Decimal
class MonthlyReportResponse(BaseModel):
    year: int
    month: int
    total_income: Decimal
    total_expense: Decimal
    balance: Decimal
class YearlyReportResponse(BaseModel):
    year: int
    total_income: Decimal
    total_expense: Decimal
    balance: Decimal