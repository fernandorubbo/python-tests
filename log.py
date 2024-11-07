import time as perftime
import logging

logger2 = logging.getLogger(__name__)

def log_exec_time(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = perftime.perf_counter()
            result = func(*args, **kwargs)
            end_time = perftime.perf_counter()
            execution_time = end_time - start_time
            logger.info("Function %s - Execution time: %.4f seconds",
                         func.__name__, execution_time)
            logger2.info("local logger")
            return result
        return wrapper
    return decorator
