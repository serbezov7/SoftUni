first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}

functions = {
    "Add First": lambda x: [first.add(el) for el in x],
    "Add Second": lambda x: [second.add(el) for el in x],
    "Remove First": lambda x: [first.discard(el) for el in x],
    "Remove Second": lambda x: [second.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)
}

for _ in range(int(input())):
    command, *data = input().split()
    current_command = command + " " + data.pop(0)

    if data:
        functions[current_command](int(x) for x in data)
    else:
        functions[current_command]()

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
