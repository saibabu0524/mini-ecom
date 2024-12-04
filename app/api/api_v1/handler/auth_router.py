from fastapi import APIRouter

from app.api.api_v1.handler.singup_route import signup_router
from app.core.constants import AUTH_ROUTE_TAG
from app.model.config import settings

auth_router = APIRouter(prefix=settings.AuthURL,tags=[AUTH_ROUTE_TAG])


auth_router.include_router(router=signup_router)