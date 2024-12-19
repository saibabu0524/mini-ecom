from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # Automatically load environment variables from a .env file
        env_file_encoding = "utf-8"


settings = Settings()
