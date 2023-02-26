import logging


LOG_FORMAT = "%(asctime)s %(levelname)s  - %(message)s"

logging.basicConfig(filename='logfile.log',level= logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()