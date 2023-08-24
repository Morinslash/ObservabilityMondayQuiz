# logger_config.py

import logging

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = getattr(RequestState, "correlation_id", "no-id")
        return True

class RequestState:
    correlation_id = ""

# Set up the logger
logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)
logger.addFilter(ContextFilter())
