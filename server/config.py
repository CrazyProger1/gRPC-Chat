import logging
import os
from datetime import timedelta

SECRET = os.getenv("SECRET", "qwejkqwjekqjwekj")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 50052)
ADDRESS = f"{HOST}:{PORT}"
MAX_WORKERS = 10
LOGGING_FILE = "server.log"
LOGGING_LEVEL = logging.INFO
LOGGING_FMT = (
    "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)
LOGGING_DATEFMT = "%d/%b/%Y %H:%M:%S"
DATABASE_URI = "sqlite:///database.db"
JWT_ACCESS_LIFETIME = timedelta(days=1)
JWT_REFRESH_LIFETIME = timedelta(days=30)
