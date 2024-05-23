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

HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 50051)
MAX_WORKERS = 10
LOGGING_FILE = "server.log"
LOGGING_LEVEL = logging.INFO


def configure_logging():
    logging.basicConfig(
        filename=LOGGING_FILE,
        encoding="utf-8",
        level=LOGGING_LEVEL,
        filemode="w",
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
    )


def runserver():
    server = grpc.server(
        thread_pool=futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
        interceptors=(LoggingInterceptor(),),
    )
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port(f"{HOST}:{PORT}")
    server.start()
    server.wait_for_termination()


def main():
    configure_logging()
    runserver()


if __name__ == "__main__":
    main()
