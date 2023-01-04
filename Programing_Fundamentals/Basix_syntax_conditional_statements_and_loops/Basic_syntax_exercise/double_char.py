command = input()

while command != "End":
    current_string = command
    if current_string == "SoftUni":
        command = input()
        continue
    for word in current_string:
        print(word * 2, end="")
    print()

    command = input()
