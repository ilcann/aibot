from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    nestjs_api_url: str = "http://localhost:3002"
    fastapi_host: str = "0.0.0.0"
    fastapi_port: int = 8000
    env : str = "development"  # development, production
    
    gliner_model_name: str = "urchade/gliner_large-v2.1" # default model name for GLiNER

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()