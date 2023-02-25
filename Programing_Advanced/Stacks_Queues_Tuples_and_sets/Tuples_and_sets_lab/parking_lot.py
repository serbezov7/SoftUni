number_of_commands = int(input())
parking_set = set()

for _ in range(number_of_commands):
    command = input().split(", ")
    if command[0] == "IN":
        parking_set.add(command[1])
    elif command[0] == "OUT":
        if command[1] in parking_set:
            parking_set.remove(command[1])

if parking_set:
    print("\n".join(parking_set))
else:
    print("Parking Lot is Empty")