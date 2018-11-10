import logging

import config

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

f_handler = logging.FileHandler(config.LOG_LOCATION)
f_handler.setFormatter(formatter)
logger.addHandler(f_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
