import logging
from functools import wraps
from typing import Callable, Iterable

import grpc

logger = logging.getLogger("chat")


def permissions(*perms: Callable):
    def decorator(target: Callable):
        @wraps(target)
        def wrapper(*args, **kwargs):
            if all(tuple(perm(*args, **kwargs) for perm in perms)):
                return target(*args, **kwargs)

            logger.warning(f"Permission denied: {target}")
            context = args[2]
            context.abort(grpc.StatusCode.PERMISSION_DENIED, "Permission denied")

        return wrapper

    return decorator
