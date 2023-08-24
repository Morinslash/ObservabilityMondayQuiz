from fastapi import FastAPI, Request
import logging
from uuid import uuid4
from starlette.middleware.base import BaseHTTPMiddleware

logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = RequestState.correlation_id
        return True

# Define a global state for the request
class RequestState:
    correlation_id = ""

# Add the filter to the logger
logger.addFilter(ContextFilter())

app = FastAPI()

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid4()))
        request.state.correlation_id = correlation_id
        RequestState.correlation_id = correlation_id  # Set the global state
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id
        return response

app.add_middleware(CorrelationIdMiddleware)

@app.get("/")
def read_root(request: Request):
    logger.info(f"Received request from {request.client.host}")
    return {"Hello": "World"}