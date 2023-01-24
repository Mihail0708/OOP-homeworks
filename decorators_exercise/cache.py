def cache(func_repr):
    log = {}

    def wrapper(num):
        if num not in log:
            log[num] = func_repr(num)

        return func_repr(num)

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)
