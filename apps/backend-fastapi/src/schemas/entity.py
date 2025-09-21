from pydantic import BaseModel

class Entity(BaseModel):
    text: str
    label: str
    start: int | None = None
    end: int | None = None
    score: float | None = None