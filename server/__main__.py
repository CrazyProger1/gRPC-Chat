import logging
import os
from concurrent import futures

import grpc
from dotenv import load_dotenv

from gen import auth_pb2_grpc, chat_pb2_grpc
from server.interceptors.logging import LoggingInterceptor
from server.services.auth import AuthService
from server.services.chat import ChatService

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 50052)
ADDRESS = f"{HOST}:{PORT}"
MAX_WORKERS = 10
LOGGING_FILE = "server.log"
LOGGING_LEVEL = logging.INFO
LOGGING_FMT = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
LOGGING_DATEFMT = "%d/%b/%Y %H:%M:%S"
logger = logging.getLogger("chat")


def configure_logging():
    formatter = logging.Formatter(fmt=LOGGING_FMT, datefmt=LOGGING_DATEFMT)
    file_handler = logging.FileHandler(
        filename=LOGGING_FILE,
        mode="a",
        encoding="utf-8"
    )
    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.setLevel(LOGGING_LEVEL)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def runserver():
    server = grpc.server(
        thread_pool=futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
        interceptors=(LoggingInterceptor(),),
    )
    logger.info("Server initialized")

    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port(ADDRESS)

    logger.info("Starting server...")

    server.start()

    logger.info(f"Server started on {ADDRESS}")

    server.wait_for_termination()


def main():
    configure_logging()
    runserver()


if __name__ == "__main__":
    main()
