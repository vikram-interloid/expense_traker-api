from sqlalchemy.orm import Session

from app.models.category import Category,CategoryType

from app.models.user import User


def seed_categories(
    db: Session,
    users: list[User],
) -> list[Category]:

    categories = []

    for user in users:

        categories.extend(
            [
                Category(
                    name="Salary",
                    type=CategoryType.INCOME,
                    user_id=user.id,
                ),
                Category(
                    name="Food",
                    type=CategoryType.EXPENSE,
                    user_id=user.id,
                ),
            ]
        )

    db.add_all(categories)
    db.commit()

    for category in categories:
        db.refresh(category)

    print("20 categories seeded successfully.")

    return categories