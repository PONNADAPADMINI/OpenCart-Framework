import logging
import os
from logging.handlers import RotatingFileHandler

class LogGen:

    @staticmethod
    def logGen():

        logger = logging.getLogger("selenium")
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.DEBUG)
        # logger.setLevel(logging.ERROR)

        #----------------CONFIGURE THE LOGGER. ----------------
        if not logger.handlers:
            log_dir = os.path.join(os.getcwd(), "logs")
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, "automation.log")

            # rotating file handler - Max 5m limit -3 count.
            file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024,backupCount=3)
            format_str = '%(asctime)s: %(levelname)s: %(message)s'
            date_format = '%m/%d/%Y %I:%M:%S %p'

            formatter = logging.Formatter(format_str,datefmt=date_format)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.addHandler(file_handler)
        return logger



