import logging
import os


class Logger:
    """
    Centralized logger for the calculator application.
    """

    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger is None:

            log_file = os.getenv("CALCULATOR_LOG_FILE", "calculator.log")

            logger = logging.getLogger("calculator")
            logger.setLevel(logging.INFO)

            # IMPORTANT: prevent duplicate handlers
            if not logger.handlers:

                file_handler = logging.FileHandler(log_file)
                file_handler.setLevel(logging.INFO)

                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
                file_handler.setFormatter(formatter)

                logger.addHandler(file_handler)

            logger.propagate = False

            cls._logger = logger

        return cls._logger