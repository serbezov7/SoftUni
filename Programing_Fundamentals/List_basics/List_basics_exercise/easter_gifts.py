gifts = input().split()
command = input()
# filtered_list = []
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        if command[1] in gifts:
            for i in range(len(gifts)):
                if gifts[i] == command[1]:
                    gifts[i] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input()
while "None" in gifts:
    gifts.remove("None")
# for j in gifts:
#     if j != "None":
#         filtered_list.append(j)
print(" ".join(gifts))
