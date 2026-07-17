from fastapi import HTTPException, status
from uuid import UUID

from app.models.category import Category
from app.models.user import User
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import (
    CategoryCreateRequest,
    CategoryUpdateRequest,
    CategoryListResponse,
    UpdateCategoryResponse,
    )
from app.schemas.auth import MessageResponse

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
        category = self.repository.get_category(
            name=request.name,
            category_type=request.type,
            user_id=current_user.id,
        )
        if category:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Category already exists",
            )
        category = Category(
            name=request.name,
            type=request.type,
            user_id=current_user.id,
            )
        category = self.repository.create_category(category)
        
        return {
            "message": "Category created successfully",
            "data": category,
        }
        
        # return CategoryListResponse.model_validate(category)
        
    def get_categories(
        self,
        current_user: User,
        ) -> CategoryListResponse:
        categories = self.repository.get_categories(
            current_user.id,
        )
        return{
            "data": categories,
        }
    def get_category(
        self,
        category_id: UUID,
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
    
    
    def update_category(
        self,
        category_id: UUID,
        request: CategoryUpdateRequest,
        current_user: User,
    ) -> UpdateCategoryResponse:
        category = self.repository.get_category_by_id(
            category_id,
            current_user.id,
        )
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
                )
        duplicate = self.repository.update_category_by_id(
            name=request.name,
            # category_type=request.type,
            user_id=current_user.id,
        )
        if (
            duplicate is not None
            and duplicate.id != category.id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Category already exists",
            )

        category.name = request.name
        # category.type = request.type
        category = self.repository.update_category(
        category,
        )
        
        return {
        "message": "Category updated successfully",
        "data": category,
        }
        
        
    def delete_category(
    self,
    category_id: UUID,
    current_user: User,
    ) -> None:
        category = self.repository.get_category_by_id(
            category_id,
            current_user.id,
        )
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )
            
        if self.repository.category_has_transactions(
            category_id
        ):
            
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail= "category cannot be deleted because it has a associated transacation ",
            )
        self.repository.delete_category(category)
        return MessageResponse(
            message= "category deleted sucessfully"
        )