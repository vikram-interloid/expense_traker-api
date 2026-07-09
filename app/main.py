# from fastapi import FastAPI,
# from app.services.auth_service import AuthService
# from app.repositories.auth_repository import AuthRepository
# # from app.exceptions.handlers import register_exception_handlers

# from app.core.config import settings

# from app.api.v1.health import router as health_router
# auth = AuthService(AuthRepository)
# app = FastAPI(
#     title=settings.app_name,
#     version=settings.app_version,
# )




# router =APIRouter(prefix="/v1/api")


# @router.get('/users/register')
# def Register(username,email,password):
#     return auth.register(username="anmal",email=email, password=password)
    
    
    
# app.include_router(router)



# # @router.get("/uesrs")
# # def get_users()

from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.health import router as health_router
from app.core.config import settings
from app.api.v1.category import router as category_router
# from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

# register_exception_handlers(app)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(category_router)