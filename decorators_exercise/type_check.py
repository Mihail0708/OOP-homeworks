def type_check(kind):
    def decorator(func_repr):
        def wrapper(*args):
            if type(*args) != kind:
                return 'Bad Type'

            return func_repr(*args)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
