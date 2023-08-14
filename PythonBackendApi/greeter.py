class Greeter:
    def __init__(self, logger):
        self.logger = logger

    def get_greeting(self):
        self.logger.info(f"invoked the get_greeting method.")
        return "Hello, World!"
