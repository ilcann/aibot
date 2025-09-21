from pydantic.generics import GenericModel
from fastapi.responses import JSONResponse
from functools import wraps
from src.models.response import StandardResponse

def standard_response():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)

            # Zorunlu alan kontrolü
            if not isinstance(result, dict) or "data" not in result or "message" not in result:
                raise ValueError("Endpoint must return dict with 'data' and 'message'")

            data = result["data"]
            message = result["message"]

            # HTTP status kodu ve success logic
            status_code = result.get("statusCode", 200)
            success = 200 <= status_code < 300

            # Eğer data Pydantic model ise direkt, değilse dict
            response_content = StandardResponse(
                success=success,
                statusCode=status_code,
                message=message,
                data=data
            ).dict()

            return JSONResponse(content=response_content, status_code=status_code)

        return wrapper
    return decorator
