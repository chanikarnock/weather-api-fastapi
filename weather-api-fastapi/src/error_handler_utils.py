from http import HTTPStatus
import json
from settings import logger

from fastapi import Response

from src.default_serializer import DefaultResponseSerializer

class ErrorHandlerUtil:
    def handle_error_response(exception, default_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        """Generate a standardized error response."""
        logger.error(f"Error handling: {exception}")
        response_entity = DefaultResponseSerializer(
            code=getattr(exception, "http_status_code", default_code),
            status="FAIL",
            message=getattr(exception, "message", "An unexpected error occurred.")
        )
        return Response(
            status_code=response_entity.code,
            content=json.dumps(response_entity.dict()),
            media_type="application/json",
        )