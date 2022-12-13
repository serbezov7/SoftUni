number = int(input())
sum = 0
for numbers in range(number):
    current_number = int(input())
    sum += current_number
average = sum / number
print(f"{average:.2f}")