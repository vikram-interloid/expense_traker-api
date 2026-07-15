from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import Category, CategoryType

class CategoryRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_category(
        self,
        name: str,
        category_type: CategoryType,
        user_id: int,
    ) -> Category | None:

        stmt = select(Category).where(
            Category.name == name,
            Category.type == category_type,
            Category.user_id == user_id,
        )

        return self.db.scalar(stmt)

    def create_category(
        self,
        category: Category,
    ) -> Category:

        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category


    def get_categories(
        self,
        user_id: int,
    ) -> list[Category]:
        stmt = (
            select(Category)
            .where(Category.user_id == user_id)
            .order_by(Category.id)
        )
        return list(self.db.scalars(stmt).all())
    
    
    def get_category_by_id(
        self,
        category_id: int,user_id: int,
        ) -> Category | None:
        stmt = (
            select(Category)
            .where(
                Category.id == category_id,
                Category.user_id == user_id,
                )
            )
        return self.db.scalar(stmt)
    
    def update_category(
        self,
        category: Category,
        ) -> Category:
        self.db.commit()
        self.db.refresh(category)
        return category
    
    def delete_category(
    self,
    category: Category,
    ) -> None:
        self.db.delete(category)
        self.db.commit()
    