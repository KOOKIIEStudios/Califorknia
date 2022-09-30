"""Generic logger module

Business logic from: https://www.toptal.com/python/in-depth-python-logging
This is a wrapper Python's built-in logger.
"""
from pathlib import Path
import sys
import logging
from logging.handlers import TimedRotatingFileHandler

# Use a config file for these, in larger projects:
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
FORMATTER = logging.Formatter(LOG_FORMAT)
LOG_DIR_PATH_1 = Path("logs")
LOG_DIR_PATH_2 = Path("califorknia/logs")


def get_log_path():
    if LOG_DIR_PATH_1.exists():
        return Path(LOG_DIR_PATH_1, "califorknia.log")
    return Path(LOG_DIR_PATH_2, "califorknia.log")


def get_console_handler() -> logging.Handler:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler() -> logging.Handler:
    file_handler = TimedRotatingFileHandler(get_log_path(), when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


class NullHandler(logging.Handler):
    """Silent handler"""

    def emit(self, record):
        pass


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Use silent handler if you want to be able to turn logging on and off:
    # Instantiate with a silent handler that doesn't return anything, since
    # the logger object from the logging module REQUIRES at least ONE handler
    # h = NullHandler()
    # logger.addHandler(h)

    # Use default handler in this method, to always have logging on by default:
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    return logger


def shutdown_logger() -> None:
    logging.shutdown()
    