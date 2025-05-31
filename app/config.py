from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(default="postgresql://auth_user:auth_password@localhost:5432/user_auth")
    SECRET_KEY: str = Field(default="your-secret-key-here")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)

    class Config:
        env_file = ".env"

settings = Settings()