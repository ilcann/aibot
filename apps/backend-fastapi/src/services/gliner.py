from gliner import GLiNER
from src.core import settings
from src.models import label_store
from src.schemas import Entity
from typing import List
from src.core.exceptions import AppException, ValidationException

class GlinerService:
    def __init__(self):
        self.model = GLiNER.from_pretrained(settings.gliner_model_name)
        self.labels = label_store.get()
    
    def extract_entities(self, text: str) -> List[Entity]:
        if not text:
            raise ValidationException("Text cannot be empty.")
        if not self.labels:
            return []
        
        try:
            entities = self.model.predict_entities(text, threshold=0.5, labels=self.labels)
        except Exception as e:
            raise AppException(f"Error occurred while extracting entities: {str(e)}")

        return [Entity(start=ent.start, end=ent.end, label=ent.label, text=ent.text) for ent in entities]
    
gliner_service = GlinerService()