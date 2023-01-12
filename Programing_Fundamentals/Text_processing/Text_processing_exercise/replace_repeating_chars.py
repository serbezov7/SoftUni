some_string = input()
last_letter = ""
new_string = ""
for index in range(len(some_string)):
    if some_string[index] == last_letter:
        continue
    new_string += some_string[index]
    last_letter = some_string[index]

print(new_string)