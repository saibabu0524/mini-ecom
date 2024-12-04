from fastapi import APIRouter
from app.core.routes import routes
from app.model.models import SignUpRequest

signup_router = APIRouter()


@signup_router.put(path=routes.USER_SIGN_UP)
async def user_sign_up(request : SignUpRequest) :
    return {
        "request" : f"${request}",
        "status" : "success"
    }