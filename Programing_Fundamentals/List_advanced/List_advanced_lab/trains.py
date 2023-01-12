wagons = int(input())
train_list = [0] * wagons
command = input().split()

while command[0] != "End":
    current_command = command[0]
    if current_command == "add":
        count_people = int(command[1])
        train_list[-1] += count_people
    elif current_command == "insert":
        index = int(command[1])
        value = int(command[2])
        train_list[index] += value
    elif current_command == "leave":
        index = int(command[1])
        value = int(command[2])
        train_list[index] -= value

    command = input().split()

print(train_list)

