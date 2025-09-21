from pydantic.generics import GenericModel
from fastapi.responses import JSONResponse
from functools import wraps
from models.response import StandardResponse

# Wrapper decorator
def standard_response():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            if not isinstance(result, dict) or "data" not in result or "message" not in result:
                raise ValueError("Endpoint must return dict with 'data' and 'message'")
            
            # data Pydantic modeline sar
            response_model = result.get("response_model")  # opsiyonel, endpoint belirtebilir
            data = result["data"]
            if response_model:
                data = response_model(**data) if isinstance(data, dict) else response_model(data)

            return JSONResponse(content=StandardResponse[data.__class__](
                data=data,
                message=result["message"]
            ).dict())
        return wrapper
    return decorator