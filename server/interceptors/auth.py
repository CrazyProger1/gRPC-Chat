import logging
from typing import Callable

import grpc

logger = logging.getLogger("chat")


class AuthInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation: Callable, handler_call_details):
        response = continuation(handler_call_details)
        return response
