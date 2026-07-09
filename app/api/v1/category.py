from fastapi import APIRouter, Depends, status

from app.core.dependencies import (
    get_category_service,
    get_current_user,
)
from app.models.user import User
from app.schemas.category import (
    CategoryCreateRequest,
    CategoryResponse,
)
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
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
    response_model=list[CategoryResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    return service.get_categories(
        current_user,
    )
    
@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
)
def get_category(
    category_id: int,
    current_user: User = Depends(get_current_user),
    service: CategoryService = Depends(get_category_service),
):
    return service.get_category(
        category_id,
        current_user,
    )
    

