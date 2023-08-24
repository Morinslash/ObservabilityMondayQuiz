from logger_config import logger

class HelloWorldService:
    def get_greeting(self):
        logger.info("Generating greeting")
        return {"Hello": "World"}
