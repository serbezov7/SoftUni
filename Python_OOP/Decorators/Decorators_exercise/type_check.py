def type_check(type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, type):
                return func(arg)
            return "Bad Type"

        return wrapper

    return decorator
