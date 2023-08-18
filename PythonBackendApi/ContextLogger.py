import logging

class ContextLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.correlation_id = None

    def set_correlation_id(self, correlation_id):
        self.correlation_id = correlation_id

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        if extra is None:
            extra = {}
        # Ensure correlation_id is always present in the log record
        extra['correlation_id'] = self.correlation_id or 'N/A'
        super()._log(level, msg, args, exc_info, extra, stack_info)
