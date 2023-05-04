def squares(number):
    for num in range(1, number + 1):
        yield num ** 2


print(list(squares(5)))
