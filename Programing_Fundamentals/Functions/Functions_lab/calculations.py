def calculate_func(number_a, number_b, operation):
    if operator == "multiply":
        return number_a * number_b
    elif operator == "divide":
        return int(number_a / number_b)
    elif operator == "add":
        return number_a + number_b
    elif operator == "subtract":
        return number_a - number_b


operator = input()
first_num = int(input())
second_num = int(input())
print(calculate_func(first_num, second_num, operator))
