from typing import Optional
from pydantic import BaseModel
class LabelDto(BaseModel):
    key:str
    name:str
    description: Optional[str] = None