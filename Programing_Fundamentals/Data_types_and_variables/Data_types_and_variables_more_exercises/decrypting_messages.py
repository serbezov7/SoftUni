key = int(input())
lines = int(input())

for letter in range(lines):
    current_letter = ord(input()) + key
    final_letter = chr(current_letter)
    print(final_letter, end="")
