from collections import deque

expression = input().split()
numbers = deque()

operators = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

for ch in expression:
    if ch in "*/+-":
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = operators[ch](first_num, second_num)
            numbers.appendleft(result)
    else:
        numbers.append(int(ch))
print(numbers[0])


# from functools import reduce
#
# expression = input().split()
# idx = 0
#
# operators = {
#     "*": lambda x: reduce(lambda a, b: a * b, map(int, expression[:x])),
#     "+": lambda x: reduce(lambda a, b: a + b, map(int, expression[:x])),
#     "-": lambda x: reduce(lambda a, b: a - b, map(int, expression[:x])),
#     "/": lambda x: reduce(lambda a, b: a // b, map(int, expression[:x])),
#
# }
#
# while len(expression) > idx:
#     element = expression[idx]
#
#     if element in "*+-/":
#         expression[0] = operators[element](idx)
#         [expression.pop(1) for _ in range(idx)]
#         idx = 0
#
#     idx += 1
#
# print(expression[0])

