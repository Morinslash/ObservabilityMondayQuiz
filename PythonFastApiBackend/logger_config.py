import logging

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = getattr(RequestState, "correlation_id", "no-id")
        return True

class RequestState:
    correlation_id = ""

def get_logger(name=None):
    logger = logging.getLogger(name if name else __name__)
    logger.addFilter(ContextFilter())
    return logger
