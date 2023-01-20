import logging

class Logger:
    def __init__(self, name, file_name='../log.txt'):
        # Create a logger with the given name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Create a file handler for the log file
        self.handler = logging.FileHandler(file_name)
        self.handler.setLevel(logging.INFO)

        # Create a log format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(self.handler)

    def log(self, message):
        # Log the given message
        self.logger.info(message)

# Usage
if __name__ == "__main__":
    logger = Logger(__name__)
    logger.log("This is a test log message.")