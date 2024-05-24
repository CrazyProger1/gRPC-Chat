import logging
import os

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
