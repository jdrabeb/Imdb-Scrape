from functools import wraps
import logging
import time

def create_logger():
    logging.basicConfig(filename="logs.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

    logger = logging.getLogger('Web_Scrapping')
    return logger

'''
Decorator that logs the name of the function
and the time it's been running for
'''
def timed(enabled):
    def dec_timed(func):
        if enabled:
            def exec_time(*args, **kwargs):
                logger = create_logger()
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                logger.info("{} ran in {}s".format(func.__name__, round(end - start, 2)))
                return result
            return exec_time
        else:
            return func
    return dec_timed

