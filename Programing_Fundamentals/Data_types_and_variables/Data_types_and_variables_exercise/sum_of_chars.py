lines = int(input())
total_sum = 0

for char in range(lines):
    current_char = input()
    total_sum += (ord(current_char))
print(f"The sum equals: {total_sum}")
