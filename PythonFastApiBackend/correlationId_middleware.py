from fastapi import Request
from uuid import uuid4
from starlette.middleware.base import BaseHTTPMiddleware
from logger_config import RequestState

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid4()))
        request.state.correlation_id = correlation_id
        RequestState.correlation_id = correlation_id 
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id
        return response