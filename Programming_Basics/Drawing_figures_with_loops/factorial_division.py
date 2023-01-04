def fact_division(num1, num2):
    sum_first = num1
    sum_second = num2
    for current_num in range(1, num1):
        sum_first *= current_num
    for current_num in range(1, num2):
        sum_second *= current_num
    result = sum_first / sum_second
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())
print(fact_division(first_number, second_number))
