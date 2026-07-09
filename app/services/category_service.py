from fastapi import HTTPException, status

from app.models.category import Category
from app.models.user import User
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreateRequest


class CategoryService:

    def __init__(
        self,
        repository: CategoryRepository,
    ):
        self.repository = repository

    def create_category(
        self,
        request: CategoryCreateRequest,
        current_user: User,
    ) -> Category:

        category = self.repository.get_category_by_name(
            request.name,
            current_user.id,
        )

        if category:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Category already exists",
            )

        new_category = Category(
            name=request.name,
            type=request.type,
            user_id=current_user.id,
        )

        return self.repository.create_category(
            new_category,
        )
        
    def get_categories(
        self,
        current_user: User,
        ) -> list[Category]:
        return self.repository.get_categories(
            current_user.id,
        )
    def get_category(
        self,
        category_id: int,
        current_user: User,
        ) -> Category:
        category = self.repository.get_category_by_id(
            category_id,
            current_user.id,
            )
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )
        return category