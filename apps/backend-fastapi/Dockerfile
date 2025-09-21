# 1. Base image
FROM pytorch/pytorch

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
