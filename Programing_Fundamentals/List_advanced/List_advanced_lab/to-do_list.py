command = input().split("-")
to_do_list = []

while command[0] != "End":
    importance = int(command[0])
    note = command[1]
    to_do_list.append((importance, note))

    command = input().split("-")

filtered_list = [x[1] for x in sorted(to_do_list)]
print(filtered_list)
