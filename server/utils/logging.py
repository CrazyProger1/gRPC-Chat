import inspect
import logging
from functools import wraps
from typing import Callable, Iterable

logger = logging.getLogger("chat")


def catch(
    target: Callable = None,
    /,
    *,
    exceptions: Iterable[type] = (Exception,),
    retval: any = None,
    handler: Callable[[Exception], any] = None,
    onlylog: bool = False,
):
    async def async_wrapper(*args, **kwargs):
        try:
            return await target(*args, **kwargs)
        except Exception as e:
            if not isinstance(e, *exceptions) or onlylog:
                logger.error(f"Error occurred: {type(e).__name__}: {e}")
                raise e
            logger.warning(f"Error caught: {type(e).__name__}: {e}")
            if inspect.iscoroutinefunction(handler):
                return await handler(e) or retval
            elif catch(handler):
                return handler(e) or retval
            return retval

    def sync_wrapper(*args, **kwargs):
        try:
            return target(*args, **kwargs)
        except Exception as e:
            if not isinstance(e, *exceptions) or onlylog:
                logger.error(f"Error occurred: {type(e).__name__}: {e}")
                raise e
            logger.warning(f"Error caught: {type(e).__name__}: {e}")
            if callable(handler):
                return handler(e) or retval
            return retval

    def decorator(func: Callable):
        nonlocal target

        target = func

        if inspect.iscoroutinefunction(target):
            return wraps(target)(async_wrapper)
        return wraps(target)(sync_wrapper)

    if target is None:
        return decorator

    return decorator(target)
