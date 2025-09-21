# 1. Base image
FROM pytorch/pytorch

# 2. Çalışma dizini
WORKDIR /app

# 4. uv kur
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# 5. Uv dosyalarını kopyala
COPY pyproject.toml uv.lock* /app/

# 6. Dependencies yükle
RUN uv sync

# 7. Kodları kopyala
COPY ./src /app/src

# 8. Port expose
EXPOSE 8000

# 9. Uvicorn ile FastAPI başlat
CMD ["python", "src/run.py"]
