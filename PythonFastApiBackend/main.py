from fastapi import FastAPI, Request
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    logger.info(f"Received request from {request.client.host}")
    return {"Hello": "World"}