import logging.config
import uuid
from flask import Flask, g

from ContextLogger import ContextLogger
from greeter import Greeter
from logConfig import LOGGING_CONFIG

# Register the custom logger class
logging.setLoggerClass(ContextLogger)

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('my_flask_app')

app = Flask(__name__)
greeter = Greeter()
@app.before_request
def before_request():
    correlation_id = str(uuid.uuid4())
    g.correlation_id = correlation_id
    logger.set_correlation_id(correlation_id)
    logger.info("Received new request")

@app.route('/')
def hello_world():
    greeting = greeter.get_greeting()
    class_name = greeter.__class__.__name__
    logger.info(f"Serving greeting from class {class_name}: {greeting}")
    return greeting


if __name__ == '__main__':
    app.run(debug=True)
