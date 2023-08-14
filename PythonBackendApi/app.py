import logging.config

from flask import Flask

from greeter import Greeter
from logConfig import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

app = Flask(__name__)
greeter = Greeter(app.logger)


@app.route('/')
def hello_world():
    greeting = greeter.get_greeting()
    class_name = greeter.__class__.__name__
    app.logger.info(f"Serving greeting from class {class_name}: {greeting}")
    return greeting


if __name__ == '__main__':
    app.run(debug=True)
