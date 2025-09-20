# 1. Base image
FROM python:3.12-slim

# 2. Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3. Poetry kur
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# 4. Çalışma dizini
WORKDIR /app

# 5. Poetry dosyalarını kopyala
COPY pyproject.toml poetry.lock* ./

# 6. Dependencies yükle (virtualenv devre dışı, container içinde direkt)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# 7. Kodları kopyala
COPY . .

# 8. Port expose
EXPOSE 8000

# 9. Uvicorn ile FastAPI başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
