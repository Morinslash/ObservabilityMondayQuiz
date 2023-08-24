from fastapi import FastAPI, Request
from uuid import uuid4
from starlette.middleware.base import BaseHTTPMiddleware
from helloService import HelloWorldService
from logger_config import logger, RequestState, ContextFilter  # Import from logger_config

# No need to redefine ContextFilter, RequestState, and logger setup here

app = FastAPI()

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid4()))
        request.state.correlation_id = correlation_id
        RequestState.correlation_id = correlation_id  # Use the RequestState from logger_config
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id
        return response

app.add_middleware(CorrelationIdMiddleware)
hello_service = HelloWorldService()

@app.get("/")
def read_root(request: Request):
    logger.info(f"Received request from {request.client.host}")  # Use the logger from logger_config
    return hello_service.get_greeting()
