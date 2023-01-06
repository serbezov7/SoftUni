border = int(input())

for number in range(1, border + 1):
    sum_of_numbers = 0
    current_number = str(number)
    for str_number in range(len(current_number)):
        sum_of_numbers += int(current_number[str_number])
    if sum_of_numbers == 5 or sum_of_numbers == 7 or sum_of_numbers == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")


# n = int(input())
#
# for number in range(1, n + 1):
#     sum_of_numbers = 0
#     digit = number
#     while digit > 0:
#         sum_of_numbers += digit % 10
#         digit = int(digit / 10)
#     if sum_of_numbers == 5 or sum_of_numbers == 7 or sum_of_numbers == 11:
#         print('True')
#     else:
#         print('False')