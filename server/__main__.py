import logging
from concurrent import futures

import grpc
from dotenv import load_dotenv

from gen import auth_pb2_grpc, chat_pb2_grpc
from server.config import (
    ADDRESS,
    LOGGING_DATEFMT,
    LOGGING_FILE,
    LOGGING_FMT,
    LOGGING_LEVEL,
    MAX_WORKERS,
)
from server.database.engine import engine
from server.database.models import metadata
from server.database.repositories.message import MessageRepository
from server.database.repositories.user import UserRepository
from server.interceptors.auth import JWTAuthInterceptor
from server.interceptors.logging import LoggingInterceptor
from server.services.auth import AuthService
from server.services.chat import ChatService

load_dotenv()

logger = logging.getLogger("chat")


def configure_logging():
    formatter = logging.Formatter(fmt=LOGGING_FMT, datefmt=LOGGING_DATEFMT)
    file_handler = logging.FileHandler(
        filename=LOGGING_FILE, mode="a", encoding="utf-8"
    )
    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.setLevel(LOGGING_LEVEL)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def init_db():
    logger.info("Initializing database...")

    metadata.create_all(engine)

    logger.info("Tables created")


def runserver():
    user_repository = UserRepository(engine=engine)
    message_repository = MessageRepository(engine=engine)

    server = grpc.server(
        thread_pool=futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
        interceptors=(
            LoggingInterceptor(),
            JWTAuthInterceptor(repository=user_repository),
        ),
    )
    logger.info("Server initialized")

    chat_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatService(repository=message_repository), server
    )
    auth_pb2_grpc.add_AuthServiceServicer_to_server(
        AuthService(repository=user_repository), server
    )
    server.add_insecure_port(ADDRESS)

    logger.info("Starting server...")

    server.start()

    logger.info(f"Server started on {ADDRESS}")

    server.wait_for_termination()


def main():
    configure_logging()
    init_db()
    runserver()


if __name__ == "__main__":
    main()
