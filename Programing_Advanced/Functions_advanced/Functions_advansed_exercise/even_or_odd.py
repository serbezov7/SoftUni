def even_odd(*args):
    command = args[-1]
    if command == "even":
        even = [num for num in args[:-1] if num % 2 == 0]
        return even
    elif command == "odd":
        odd = list(filter(lambda x: x % 2 != 0, args[:-1]))
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))