some_string = input()
strength = 0
new_string = ""

for index in range(len(some_string)):
    if some_string[index] == ">":
        strength += int(some_string[index + 1])
        new_string += ">"
    elif strength > 0 and some_string[index] != ">":
        strength -= 1
    else:
        new_string += some_string[index]
print(new_string)
