from functools import wraps
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

'''
Decorator that logs the name of the function
and the time it's been running for
'''
def timed(enabled):
    def dec_timed(func):
        if enabled:
            def exec_time(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                logger.info("{} ran in {}s".format(func.__name__, round(end - start, 2)))
                return result
            return exec_time
        else:
            return func
    return dec_timed

