class store_results:

    def __init__(self, func_rep):
        self.func_rep = func_rep

    def __call__(self, *args):
        text = f"Function '{self.func_rep.__name__}' was called. Result: {self.func_rep(*args)}\n"
        with open("results.txt", "a") as file:
            file.write(text)

        return self.func_rep(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
