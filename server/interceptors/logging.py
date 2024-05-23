import logging
from typing import Callable

import grpc

logger = logging.getLogger(__name__)


class LoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation: Callable, handler_call_details):
        logging.info(f"Received RPC call: {handler_call_details.method}")

        response = continuation(handler_call_details)

        logging.info(f"Completed RPC call: {handler_call_details.method}")

        return response
