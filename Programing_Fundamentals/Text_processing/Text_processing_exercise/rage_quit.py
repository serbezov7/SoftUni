some_string = input().upper()
digit = ""
new_string = ""
unique_symbols = []
string = ""
for index in range(len(some_string)):
    if some_string[index].isdigit():
        if index + 1 in range(len(some_string)) and some_string[index + 1].isdigit():
            digit += some_string[index]
            digit += some_string[index + 1]
            new_string += int(digit) * string
            digit = ""
        else:
            new_string += int(some_string[index]) * string
        string = ""
    else:
        if some_string[index] not in unique_symbols:
            unique_symbols.append(some_string[index])
        string += some_string[index]
print(f"Unique symbols used: {len(unique_symbols)}")
print(new_string)