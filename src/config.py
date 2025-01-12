from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_HOST: str = "localhost"
    API_PORT: int = 8000
    DATABASE_URL: str
    NBA_STATS_API_KEY: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"

settings = Settings()