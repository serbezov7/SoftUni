numbers = list(map(int, input().split()))
count = int(input())

for current_number in range(count):
    numbers.remove(min(numbers))
numbers_as_string = []
for number_str in numbers:
    numbers_as_string.append(str(number_str))

print(", ".join(numbers_as_string))
