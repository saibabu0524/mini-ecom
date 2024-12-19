from fastapi import FastAPI, Depends

from app.api.api_v1.handler.auth_router import auth_router
from app.database import get_db

app = FastAPI()

app.include_router(auth_router)



@app.get('/')
async def root_route(db=Depends(get_db)):
    return {"status":"server is running"}