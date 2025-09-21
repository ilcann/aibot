from pydantic import BaseSettings

class Settings(BaseSettings):
    nestjs_api_url: str = "http://localhost:3000"
    fastapi_port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()