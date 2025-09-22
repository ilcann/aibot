# 1. Base image
FROM python:3.13-slim

RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# 2. Çalışma dizini
WORKDIR /app

# 5. Uv dosyalarını kopyala
COPY pyproject.toml uv.lock* /app/
    
RUN pip install .

# 7. Kodları kopyala
COPY ./src /app/src

# 8. Port expose
EXPOSE 8000

# 9. Uvicorn ile FastAPI başlat
CMD ["python", "run.py"]
