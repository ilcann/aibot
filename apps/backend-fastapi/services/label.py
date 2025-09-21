import httpx
from core import settings
from models import label_store

class LabelService:
    async def sync_labels(self) -> list[str]:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.nestjs_api_url)
            response.raise_for_status()
            resp_json = response.json()
            # labels keyName extraction
            labels_data = resp_json.get("data", {}).get("labels", [])
            keynames = [label["keyName"] for label in labels_data]

            # store update
            label_store.set(keynames)
            return keynames
    async def get_labels(self) -> list[str]:
        return label_store.get()