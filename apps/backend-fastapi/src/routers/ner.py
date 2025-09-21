from fastapi import APIRouter, Depends, HTTPException, Request, Response
from src.interceptors import standard_response
from src.models.response import ControllerResponse, ExtractEntitiesRequest, ExtractEntitiesResponse, StandardResponse
from src.services.gliner import gliner_service

router = APIRouter(prefix="/ner", tags=["NER"])

@router.post("/extract", response_model=StandardResponse[ExtractEntitiesResponse])
@standard_response()
async def extract_entities(request: ExtractEntitiesRequest):
    text = request.text
    entities = gliner_service.extract_entities(text)
    return {
        "data": ExtractEntitiesResponse(entities=entities),
        "message": "Entities extracted successfully"
    }