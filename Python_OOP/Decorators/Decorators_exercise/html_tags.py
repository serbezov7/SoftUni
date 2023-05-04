def tags(letter):
    def decorator(func):
        def wrapper(*args):
            return f"<{letter}>{func(*args)}</{letter}>"

        return wrapper

    return decorator
