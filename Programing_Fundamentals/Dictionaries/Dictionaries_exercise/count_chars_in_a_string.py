current_string = input().replace(" ", "")

char_dict = {}

for char in current_string:
    if char not in char_dict.keys():
        char_dict[char] = 0
    char_dict[char] += 1
for char, value in char_dict.items():
    print(f"{char} -> {value}")
