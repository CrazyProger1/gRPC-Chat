import logging
from concurrent import futures
from typing import Callable

import grpc
from dotenv import load_dotenv
from grpc_health.v1 import health, health_pb2, health_pb2_grpc

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
from server.servicers.auth import AuthServicer
from server.servicers.chat import ChatServicer

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


def configure_healthcheck(
    server: grpc.Server,
) -> Callable[[str, health_pb2.HealthCheckResponse.ServingStatus], any]:
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS,
        ),
    )

    health_pb2_grpc.add_HealthServicer_to_server(
        servicer=health_servicer,
        server=server,
    )

    def set_health(serv, status):
        logger.info(f"Health status changed for {serv}: {status}")
        health_servicer.set(serv, status)

    return set_health


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

    set_health = configure_healthcheck(server=server)

    chat_pb2_grpc.add_ChatServicerServicer_to_server(
        servicer=ChatServicer(
            message_repository=message_repository,
            user_repository=user_repository,
            set_health=set_health,
        ),
        server=server,
    )
    auth_pb2_grpc.add_AuthServicerServicer_to_server(
        servicer=AuthServicer(
            user_repository=user_repository,
            set_health=set_health,
        ),
        server=server,
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
