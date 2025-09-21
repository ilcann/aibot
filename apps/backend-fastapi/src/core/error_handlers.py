from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .exceptions import AppException
from src.models.response import StandardResponse

def add_exception_handlers(app: FastAPI):
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content=StandardResponse(
                success=False,
                message=str(exc.detail),
                data=None,
                status_code=exc.status_code
            ).dict()
        )
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=StandardResponse(
                success=False,
                message="Internal server error",
                data=None,
                status_code=500
            ).dict()
        )
