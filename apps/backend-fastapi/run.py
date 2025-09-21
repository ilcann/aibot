import uvicorn
from src.core import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",              # Docker ve LAN erişimi için
        port=settings.fastapi_port,   # .env veya defaults
        reload=settings.env == "development"  # Geliştirme modunda otomatik yeniden yükleme
    )
