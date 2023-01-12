def positive(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative(numbers):
    return [number for number in numbers if int(number) < 0]


def even(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


initial_numbers = input().split(", ")

print(f"Positive: {', '.join(positive(initial_numbers))}")
print(f"Negative: {', '.join(negative(initial_numbers))}")
print(f"Even: {', '.join(even(initial_numbers))}")
print(f"Odd: {', '.join(odd(initial_numbers))}")

# def positive(num):
#     for number in num:
#         if number >= 0:
#             positive_numbers.append(number)
#
#
# def negative(num):
#     for number in num:
#         if number < 0:
#             negative_numbers.append(number)
#
#
# def even(num):
#     for number in num:
#         if number % 2 == 0:
#             even_number.append(number)
#
#
# def odd(num):
#     for number in num:
#         if number % 2 != 0:
#             odd_numbers.append(number)
#
#
# def call_other():
#     return positive(initial_numbers), negative(initial_numbers), even(initial_numbers), odd(initial_numbers)
#
#
# initial_numbers = list(map(int, input().split(", ")))
# positive_numbers = []
# negative_numbers = []
# even_number = []
# odd_numbers = []
#
# call_other()
#
# print(f"Positive: {', '.join(str(x) for x in positive_numbers)}")
# print(f"Negative: {', '.join(str(x) for x in negative_numbers)}")
# print(f"Even: {', '.join(str(x) for x in even_number)}")
# print(f"Odd: {', '.join(str(x) for x in odd_numbers)}")


