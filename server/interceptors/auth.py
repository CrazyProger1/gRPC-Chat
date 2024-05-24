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

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:

        metadata = context.invocation_metadata()
        token = None
        context.user = None

        for key, value in metadata:
            if key == "authorization":
                token = value.split(" ")[1]
                break

        if token:
            try:
                payload = decode_token(token=token, secret_key=SECRET)
                user = self._repository.read(pk=payload["id"])
                context.user = user

                logger.info(f"User authenticated: {user}")
            except JWTError as e:
                pass

        return method(request_or_iterator, context)
