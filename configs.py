# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "9254436"))
    API_HASH = os.environ.get("API_HASH", "42665ffe4407fbc3f59c412caa9d84d3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5999105365:AAGHarGuzulh9f9HxX23PM4eTCgZIZAcwCQ")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1833209093 5845960615 5596825598))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb%2Bsrv%3A//sui%3Asui%40cluster0.fmobrpu.mongodb.net/%3FretryWrites%3Dtrue%26w%3Dmajority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""-1001898159090))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
