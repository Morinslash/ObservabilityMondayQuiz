import logging

class Greeter:
    def __init__(self):
        self.logger = logging.getLogger('my_flask_app')

    def get_greeting(self):
        self.logger.info(f"invoked the get_greeting method.")
        return "Hello, World!"
