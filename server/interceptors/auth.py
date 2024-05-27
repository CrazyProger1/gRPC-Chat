import logging
from typing import Any, Callable

import grpc
import grpc_interceptor

from server.config import SECRET
from server.database.repositories.user import UserRepository
from server.utils.exceptions import JWTError
from server.utils.jwt import decode_token

logger = logging.getLogger("chat")


class JWTAuthInterceptor(grpc_interceptor.ServerInterceptor):
    def __init__(self, repository: UserRepository):
        self._repository = repository

    @staticmethod
    def get_token(metadata) -> str | None:
        for key, value in metadata:
            if key == "authorization":
                try:
                    return value.split(" ")[1]
                except IndexError:
                    pass
                break

    def authenticate(self, token: str):
        if not token:
            return

        try:
            payload = decode_token(token=token, secret_key=SECRET)
            if payload.get("type") != "access":
                return
            user = self._repository.read(pk=payload["id"])
            return user
        except JWTError:
            pass

    def intercept(
            self,
            method: Callable,
            request_or_iterator: Any,
            context: grpc.ServicerContext,
            method_name: str,
    ) -> Any:

        metadata = context.invocation_metadata()
        token = self.get_token(metadata=metadata)
        context.user = self.authenticate(token=token)

        logger.info(f"Current user: {context.user}")

        return method(request_or_iterator, context)
