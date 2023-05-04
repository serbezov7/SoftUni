def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}({', '.join(str(x) for x in args)})\nit returned {func(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
