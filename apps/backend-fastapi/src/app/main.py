from fastapi import FastAPI
from app.ner.routers import ner_router

app = FastAPI( title="SecurAI FastAPI", version="1.0.0" )

app.include_router(ner_router, prefix="/ner")