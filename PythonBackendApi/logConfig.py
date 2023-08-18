import logging
from pythonjsonlogger import jsonlogger

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'json': {
            '()': jsonlogger.JsonFormatter,
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s %(correlation_id)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'level': 'DEBUG',
        }
    },
    'loggers': {
        'my_flask_app': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    }
}
