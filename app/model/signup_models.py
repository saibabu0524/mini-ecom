from typing import Any

from pydantic import BaseModel


class SignUpRequest(BaseModel):
    userName : str
    userEmail : str
    userPassword : str

class SignUpResponse(BaseModel):
    status:int
    details : Any