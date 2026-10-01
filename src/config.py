from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    redis_url: str
    openai_api_key: str = ""  # optionnel pour l'instant

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instance globale — importée partout dans le projet
# "from src.config import settings"
settings = Settings()