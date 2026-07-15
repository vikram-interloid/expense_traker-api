from datetime import date, timedelta
from decimal import Decimal
import random

from sqlalchemy.orm import Session

from app.models.category import Category, CategoryType
from app.models.transaction import Transaction
from app.models.user import User


INCOME_DESCRIPTIONS = [
    "Monthly Salary",
    "Freelance Project",
    "Bonus",
    "Interest",
    "Cashback",
]

EXPENSE_DESCRIPTIONS = [
    "Food",
    "Groceries",
    "Fuel",
    "Movie",
    "Shopping",
    "Electricity Bill",
    "Internet Bill",
    "Travel",
    "Medical",
    "Dining Out",
]


def seed_transactions(
    db: Session,
    users: list[User],
):

    transactions = []

    for user in users:

        income_category = db.query(Category).filter(
            Category.user_id == user.id,
            Category.type == CategoryType.INCOME,
        ).first()

        expense_category = db.query(Category).filter(
            Category.user_id == user.id,
            Category.type == CategoryType.EXPENSE,
        ).first()

        # Create 10 transactions for each user
        for i in range(10):

            if i % 3 == 0:
                # Income transaction
                transactions.append(
                    Transaction(
                        amount=Decimal(random.randint(20000, 80000)),
                        description=random.choice(INCOME_DESCRIPTIONS),
                        transaction_date=date.today() - timedelta(days=random.randint(1, 180)),
                        category_id=income_category.id,
                        user_id=user.id,
                    )
                )

            else:
                # Expense transaction
                transactions.append(
                    Transaction(
                        amount=Decimal(random.randint(100, 5000)),
                        description=random.choice(EXPENSE_DESCRIPTIONS),
                        transaction_date=date.today() - timedelta(days=random.randint(1, 180)),
                        category_id=expense_category.id,
                        user_id=user.id,
                    )
                )

    db.add_all(transactions)
    db.commit()

    print(f"{len(transactions)} transactions seeded successfully.")