from typing import List, Generic, TypeVar
from pydantic import BaseModel
from src.schemas import Entity

T = TypeVar("T")

class StandardResponse(BaseModel, Generic[T]):
    success: bool = True
    status_code: int = 200
    data: T
    message: str = "Success"

# POST /sync-labels response
class SyncLabelsResponse(BaseModel):
    count: int
    labels: List[str]
    
class GetLabelsResponse(BaseModel):
    labels: List[str]
    
class ExtractEntitiesResponse(BaseModel):
    entities: List[Entity]