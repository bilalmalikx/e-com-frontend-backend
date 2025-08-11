from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ecommerce-backend"
    SECRET_KEY: str = "change-me-to-a-strong-secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./ecommerce.db"

    class Config:
        env_file = ".env"

settings = Settings()
