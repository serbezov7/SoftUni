def even_odd_sum(num):
    sum_even = 0
    sum_odd = 0
    for current_num in str(num):
        current_num = int(current_num)
        if current_num % 2 == 0:
            sum_even += current_num
        else:
            sum_odd += current_num
    return sum_odd, sum_even


number = int(input())

sum_of_odd_digit, sum_of_even_digit = even_odd_sum(number)
print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digit}")
