from logger_config import get_logger

logger = get_logger(__name__)

class HelloWorldService:
    def get_greeting(self):
        logger.info("Generating greeting")
        return {"Hello": "World"}
