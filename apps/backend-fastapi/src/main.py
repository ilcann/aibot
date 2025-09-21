from src.routers import ner_router
from fastapi import FastAPI

app = FastAPI(
    title="SecurAI FastAPI",
    version="1.0.0",
)

app.include_router(ner_router, prefix="/ner")
