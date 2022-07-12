from fastapi import APIRouter

from user.api import on_after_register
from user.auth import jwt_authentication, fastapi_users

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix='/auth/jwt',
    tags=['auth']
)
router.include_router(
    fastapi_users.get_register_router(on_after_register),
    prefix='/auth',
    tags=['auth']
)
router.include_router(
    fastapi_users.get_users_router(), prefix='/users', tags=['users']
)
