def sum_numbers(first, second):
    return first + second


def subtract(first_second, third):
    return first_second - third


def add_and_subtract(first, second, third):
    first_sum = sum_numbers(first, second)
    return subtract(first_sum, third)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
