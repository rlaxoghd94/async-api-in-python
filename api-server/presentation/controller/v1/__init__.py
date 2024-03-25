from fastapi import APIRouter

from .healthcheck.health_check_controller import healthcheck_router
from .user.user_controller import user_router

__prefix = "/v1"
v1_router = APIRouter(prefix=__prefix)

v1_router.include_router(healthcheck_router)
v1_router.include_router(user_router)
