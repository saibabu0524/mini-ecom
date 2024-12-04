from fastapi import FastAPI

from app.api.api_v1.handler.auth_router import auth_router

app = FastAPI()

app.include_router(auth_router)