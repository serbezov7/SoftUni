string = input()
digits, letters, others = [], [], []

for char in string:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        others.append(char)
print("".join(digits))
print("".join(letters))
print("".join(others))
