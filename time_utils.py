from time import time, sleep


def calculate_elapsed(start):
    """
    start = time()
    sleep(4)
    elapsed, units = calculate_elapsed(start)
    
    :param start:
    :return:
    """
    elapsed = time() - start
    units = 'seconds'
    if elapsed >= 60.0:
        elapsed /= 60.0
        units = 'minutes'
    if elapsed >= 60.0:
        elapsed /= 60.0
        units = 'hours'
    return elapsed, units
