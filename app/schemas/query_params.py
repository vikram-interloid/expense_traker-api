from enum import Enum
class SortBy(str, Enum):
    AMOUNT = "amount"
    TRANSACTION_DATE = "transaction_date"
class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"