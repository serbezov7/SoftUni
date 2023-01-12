message = input().split()
my_list = []
for word in message:
    digits = ""
    text = ""
    for digit in word:
        if digit.isdigit():
            digits += str(digit)
        else:
            text += digit
    new_digit = int(digits)
    if len(text) > 1:
        my_list.append(chr(new_digit) + text[len(text) - 1:len(text)] + text[1:len(text) - 1] + text[0:1])
    else:
        my_list.append(chr(new_digit) + text)
print(" ".join(my_list))

