from src.routers import ner_router
from src.routers import label_router
from fastapi import FastAPI
from src.core import add_exception_handlers

app = FastAPI(
    title="SecurAI FastAPI",
    version="1.0.0",
)

add_exception_handlers(app)

app.include_router(ner_router)
app.include_router(label_router)
