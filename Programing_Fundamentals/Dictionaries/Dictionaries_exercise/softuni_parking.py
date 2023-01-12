def register(parking_dict_, name, plate_number_):
    if name not in parking_dict_.keys():
        parking_dict_[name] = plate_number_
        print(f"{name} registered {plate_number_} successfully")
    else:
        print(f"ERROR: already registered with plate number {plate_number_}")
    return parking_dict_


def unregister(parking_dict_, name):
    if name not in parking_dict_.keys():
        print(f"ERROR: user {name} not found")
    else:
        print(f"{name} unregistered successfully")
        del parking_dict_[name]
    return parking_dict_


parking_dict = {}
number_of_commands = int(input())

for current_command in range(number_of_commands):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        plate_number = command[2]
        parking_dict = register(parking_dict, username, plate_number)
    elif command[0] == "unregister":
        parking_dict = unregister(parking_dict, username)
for username, license_plate_number in parking_dict.items():
    print(f"{username} => {license_plate_number}")
