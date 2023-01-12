some_string = input().split()
total_sum = 0

for text in some_string:
    number = int(text[1:len(text) - 1])
    first_letter = text[0]
    last_letter = text[-1]
    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= (ord(last_letter) - 64)
    elif last_letter.islower():
        total_sum += (ord(last_letter) - 96)
print(f"{total_sum:.2f}")