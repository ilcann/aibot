from fastapi import APIRouter
from services import LabelService
from models.response import GetLabelsResponse, SyncLabelsResponse, StandardResponse
from interceptors import standard_response

router = APIRouter(prefix="/labels", tags=["Labels"])

@router.post("/sync", response_model=StandardResponse[SyncLabelsResponse])
@standard_response()
async def sync_labels():
    updated_labels = await LabelService.sync_labels()
    
    response_data = SyncLabelsResponse(
        count=len(updated_labels),
        labels=updated_labels
    )

    return SyncLabelsResponse(
        data=response_data,
        message="Labels synchronized successfully"
    )

@router.get("/", response_model=StandardResponse[GetLabelsResponse])
async def get_labels():
    labels = await LabelService.get_labels()

    response_data = GetLabelsResponse(labels=labels)

    return GetLabelsResponse(
        data=response_data,
        message="Labels retrieved successfully"
    )
