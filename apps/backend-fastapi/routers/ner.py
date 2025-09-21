from fastapi import APIRouter, Depends, HTTPException, Request, Response
from interceptors import standard_response
from models.response import ExtractEntitiesResponse, StandardResponse

ner_router = APIRouter()

@ner_router.post("/extract", response_model=StandardResponse[ExtractEntitiesResponse])
@standard_response()
async def extract_entities(request: Request):
    data = await request.json()
    text = data.get("text", "")
