from fastapi import APIRouter
from src.services import label_service
from src.models.response import ControllerResponse, GetLabelsResponse, SyncLabelsResponse, StandardResponse
from src.interceptors import standard_response

router = APIRouter(prefix="/labels", tags=["Labels"])

@router.post("/sync", response_model=StandardResponse[ControllerResponse[SyncLabelsResponse]])
@standard_response()
async def sync_labels():
    updated_labels = await label_service.sync_labels()
    
    return ControllerResponse(
        data=SyncLabelsResponse(
            count=len(updated_labels),
            labels=updated_labels
        ),
        message="Labels synchronized successfully"
    )

@router.get("/", response_model=StandardResponse[GetLabelsResponse])
@standard_response()
async def get_labels():
    labels = await label_service.get_labels()

    return {
        "data": GetLabelsResponse(labels=labels),
        "message": "Labels retrieved successfully"
    }