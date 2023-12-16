from pydantic_settings import BaseSettings
from pydantic import Field, ValidationError


class Settings(BaseSettings):
    mongo_username: str = Field(..., env="MONGO_USERNAME")
    mongo_password: str = Field(..., env="MONGO_PASSWORD")
    mongo_host: str = Field(...,env="MONGO_HOST")
    mongo_port: str = Field(...,env="MONGO_PORT")
    secret_key: str = Field(...,env="SECRET_KEY")
    algorithm: str = Field(...,env="ALGORITHM")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
try:
    settings = Settings()
except ValidationError as e:
    errors = "\n".join(f"{error['loc'][0]}: {error['msg']}" for error in e.errors())
    print(f"Environment variables validation error:\n{errors}")

settings = Settings()
