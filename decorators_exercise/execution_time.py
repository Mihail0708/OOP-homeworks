from time import time


def exec_time(func_repr):
    def wrapper(*args):
        start = time()
        func_repr(*args)
        end = time()
        total = end - start
        return total

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))
