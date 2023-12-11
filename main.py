
import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    sec = os.environ["sec"]
except KeyError:
    sec = "Token not available!"
    # logger.info("Token Manche!!!!!")
    # raise

if __name__ == "__main__":
    logger.info(f"Token value: {sec}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Rabat&country=MA')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Rabat: {temperature}')

