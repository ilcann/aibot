# 1. Base image
FROM python:3.13-slim

# 2. Çalışma dizini
WORKDIR /app

# 3. Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Poetry kur
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# 5. Uv dosyalarını kopyala
COPY pyproject.toml uv.lock* /app/

# 6. Dependencies yükle (virtualenv devre dışı, container içinde direkt)
RUN uv venv
RUN uv sync

# 7. Kodları kopyala
COPY ./src /app/src

# 8. Port expose
EXPOSE 8000

# 9. Uvicorn ile FastAPI başlat
CMD ["python", "src/run.py"]
