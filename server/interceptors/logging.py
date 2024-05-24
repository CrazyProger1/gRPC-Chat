import logging
from typing import Callable

import grpc

logger = logging.getLogger("chat")


class LoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation: Callable, handler_call_details):
        logger.info(f"Received RPC call: {handler_call_details.method}")

        response = continuation(handler_call_details)

        logger.info(f"Completed RPC call: {handler_call_details.method}")

        return response
