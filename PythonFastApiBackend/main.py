from fastapi import FastAPI, Request
from correlationId_middleware import CorrelationIdMiddleware
from helloService import HelloWorldService
from logger_config import get_logger

logger = get_logger(__name__)

app = FastAPI()

app.add_middleware(CorrelationIdMiddleware)
hello_service = HelloWorldService()

@app.get("/")
def read_root(request: Request):
    logger.info(f"Received request from {request.client.host}")
    return hello_service.get_greeting()
