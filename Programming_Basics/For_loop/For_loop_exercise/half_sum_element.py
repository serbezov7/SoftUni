import sys

numbers = int(input())
max_number = - sys.maxsize
sum_numbers = 0


for number in range(numbers):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    difference = (sum_numbers - max_number)
    print(f"Diff = {abs(max_number - difference)}")
