import logging
from typing import Any, Callable

import grpc
import grpc_interceptor

logger = logging.getLogger("chat")


class LoggingInterceptor(grpc_interceptor.ServerInterceptor):
    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:
        logger.info(f"Received RPC call: {method_name}")

        reply = method(request_or_iterator, context)

        logger.info(f"Completed RPC call: {method_name}")

        return reply
