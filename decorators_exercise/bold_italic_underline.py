def make_bold(func_rep):
    def wrapper(*args):
        return f'<b>{func_rep(*args)}</b>'
    return wrapper


def make_italic(func_rep):
    def wrapper(*args):
        return f'<i>{func_rep(*args)}</i>'
    return wrapper


def make_underline(func_rep):
    def wrapper(*args):
        return f'<u>{func_rep(*args)}</u>'
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
