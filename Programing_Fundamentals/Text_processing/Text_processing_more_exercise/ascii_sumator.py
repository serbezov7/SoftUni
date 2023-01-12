start_symbol = input()
finish_symbol = input()
some_text = input()
total_sum = 0

for char in some_text:
    if ord(char) in range(ord(start_symbol) + 1, ord(finish_symbol)):
        total_sum += ord(char)
print(total_sum)
