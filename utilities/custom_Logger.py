import logging
import os
from logging.handlers import RotatingFileHandler

class LogGen:

    @staticmethod
    def logGen():

        logger = logging.getLogger("selenium")                  #--(1)  Logger Object
        logger.setLevel(logging.INFO)                           #--(2)  To Set Level for Logging
        # logger.setLevel(logging.DEBUG)
        # logger.setLevel(logging.ERROR)

        #----------------CONFIGURE THE LOGGER. ----------------
        if not logger.handlers:                                 #--(3)  If Loop for Preventing Duplicated Handlers.
            log_dir = os.path.join(os.getcwd(), "logs")         #--(4)  Pulling the Directory of Logs files
            os.makedirs(log_dir, exist_ok=True)                 #--(4.1) Create logs directory if it doesn't exist
            log_file = os.path.join(log_dir, "automation.log")

            #(5) rotating file handler - Max 5m limit -3 count.
            file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024,backupCount=3)
            format_str = '%(asctime)s: %(levelname)s: %(message)s'#--(6) Log format: Timestamp, Log level, Message
            date_format = '%m/%d/%Y %I:%M:%S %p'

            # Initialize Formatter with  variables of date/Time & Log format.
            formatter = logging.Formatter(format_str,datefmt=date_format)
            file_handler.setFormatter(formatter)                    #--(7)  Attach Formatter to Handler
            logger.addHandler(file_handler)                         #--(8)  Attach Handler to Logger
        return logger                                               #--(9) Return the Logger object to test files - logging purposes.


        # 1️⃣ Create/Get logger object (same logger reused everywhere)
        # 2️⃣ Set log level (INFO = normal execution logs)
        # 3️⃣ Prevent duplicate handlers (important)
        # 4️⃣ Define log directory and file path
        # 5️⃣ Create rotating file handler (prevents huge log file)- MaxBytes = 5MB, backupCount = keep 3 old files
        # 6️⃣ Define log format
        # 7️⃣ Attach format to handler
        # 8️⃣ Attach handler to logger
        # 9️⃣ Return logger to use in test files


