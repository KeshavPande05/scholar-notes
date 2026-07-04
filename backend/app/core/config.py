from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Scholar Notes"

    MONGO_URL: str
    DB_NAME: str

    ADMIN_KEY: str

    CORS_ORIGINS: str = "*"

    class Config:
        env_file = ".env"


settings = Settings()
