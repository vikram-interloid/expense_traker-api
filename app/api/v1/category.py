from fastapi import APIRouter, Depends, status

from app.core.dependencies import (
    get_category_service,
    get_current_user,
)
from app.models.user import User
from app.schemas.category import (
    CategoryCreateRequest,
    CategoryResponse,
    CategoryUpdateRequest,
    CreateCategoryResponse,
    CategoryListResponse,
    UpdateCategoryResponse
)
from app.services.category_service import CategoryService
from app.schemas.auth import MessageResponse,ErrorResponse
from uuid import UUID

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "",
    response_model= CreateCategoryResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
    401: {
        "model": ErrorResponse,
        "description": "Unauthorized. Access token is missing, invalid, or expired.",
    },
    409: {
        "model": ErrorResponse,
        "description": "Category already exists.",
    },
}
    
) 
def create_category(
    request: CategoryCreateRequest,
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    return service.create_category(
        request,
        current_user,
    )
    
@router.get(
    "",
    response_model= CategoryListResponse,
    status_code=status.HTTP_200_OK,
        responses={
    401:{
        "model":ErrorResponse,
        "description":"Unauthorized",
    },
    404:{
        "model":ErrorResponse,
        "description":"Category not found",
    },
}
)
def get_categories(
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    return service.get_categories(
        current_user,
    )
    
@router.get(
    "/{id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    responses={
    401: {
        "model": ErrorResponse,
        "description": "Unauthorized. Access token is missing, invalid, or expired.",
    },
    404: {
        "model": ErrorResponse,
        "description": "Category not found.",
    },
}
)
def get_category(
    category_id: UUID,
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    return service.get_category(
        category_id,
        current_user,
    )
    
@router.put(
    "/{id}",
    response_model= UpdateCategoryResponse,
    status_code=status.HTTP_200_OK,
    responses={
    401: {
        "model": ErrorResponse,
        "description": "Unauthorized. Access token is missing, invalid, or expired.",
    },
    404: {
        "model": ErrorResponse,
        "description": "Category not found.",
    },
    409: {
        "model": ErrorResponse,
        "description": "Category name already exists.",
    },
}
)
def update_category(
    category_id: UUID,
    request: CategoryUpdateRequest,
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    return service.update_category(
        category_id,
        request,
        current_user,
    )
    
@router.delete(
    "/{id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    responses={
    401: {
        "model": ErrorResponse,
        "description": "Unauthorized. Access token is missing, invalid, or expired.",
    },
    404: {
        "model": ErrorResponse,
        "description": "Category not found.",
    },
    409: {
        "model": ErrorResponse,
        "description": "Category cannot be deleted because it has associated transactions.",
    },
}
)
def delete_category(
    category_id: UUID,
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    service.delete_category(
        category_id,
        current_user,
    )

    return MessageResponse(
        message="Category deleted successfully",
    )
    
    

