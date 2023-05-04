from collections import deque
from functools import reduce


def operate(operator, *args):
    def addition():
        return reduce(lambda x, y: x + y, args)

    def subtraction():
        return reduce(lambda x, y: x - y, args)

    def multiplication():
        return reduce(lambda x, y: x * y, args)

    def division():
        return reduce(lambda x, y: x / y if y != 0 else False, args)
        # result = 0
        # numbers = deque()
        # [numbers.append(num) for num in args]
        # first_num = numbers.popleft()
        # while numbers:
        #     second_num = numbers.popleft()
        #     if second_num != 0:
        #         result = first_num / second_num
        #         first_num = result
        # return result

    if operator == "+":
        return addition()

    elif operator == "-":
        return subtraction()

    elif operator == "*":
        return multiplication()

    elif operator == "/":
        return division()


print(operate("/", 12, 0, 4))
