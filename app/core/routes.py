from pydantic.v1 import BaseModel


class Routes(BaseModel) :
    USER_SIGN_UP = "/signin"


routes = Routes()