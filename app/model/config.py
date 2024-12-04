from pydantic.v1 import BaseSettings


class Settings(BaseSettings) :
    BaseURL : str = "api/vi"
    AuthURL : str = "/auth"



settings = Settings()
