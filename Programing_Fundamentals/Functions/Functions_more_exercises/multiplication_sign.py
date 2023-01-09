def multipl_sigh(num1, num2, num3):
    list_num = [num1, num2, num3]
    is_zero = False
    counter = 0
    for current_num in list_num:
        if current_num == 0:
            is_zero = True
            break
        elif current_num < 0:
            counter += 1

    if is_zero:
        return "zero"
    elif counter % 2 != 0:
        return "negative"
    else:
        return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multipl_sigh(first_number, second_number, third_number))
