import logging

class Logger:
    """ Logger: wrapper for logging buil-in Python lib
    Singleton design pattern to avoid Logger duplication"""
    _instance = None
    
    @classmethod
    def instance(cls, name = "", file_name='../log.txt'):
        if cls._instance is None:
            cls._instance = Logger(name, file_name)
        return cls._instance

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
    
    def error(self, message):
        self.logger.error(message)

# Usage
if __name__ == "__main__":
    logger = Logger(__name__)
    logger.log("This is a test log message.")