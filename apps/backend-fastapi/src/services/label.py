import httpx
from src.core import settings
from src.models import label_store
from src.core.exceptions import AppException

class LabelService:
    async def sync_labels(self) -> list[str]:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(settings.nestjs_api_url)
                response.raise_for_status()
                resp_json = response.json()
        except httpx.HTTPStatusError as exc:
            raise AppException(f"HTTP error while fetching labels: {exc.response.status_code}")
        except httpx.RequestError as exc:
            raise AppException(f"Request failed: {str(exc)}")

        # labels keyName extraction
        labels_data = resp_json.get("data", {}).get("labels", [])
        keynames = [label["keyName"] for label in labels_data]
        
        # store update
        label_store.set(keynames)

        return keynames
    async def get_labels(self) -> list[str]:
        return label_store.get()
    
label_service = LabelService()