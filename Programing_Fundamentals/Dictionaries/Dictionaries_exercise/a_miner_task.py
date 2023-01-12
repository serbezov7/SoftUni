command = input()
resources_dict = {}

while True:
    if command == "stop":
        break
    resource = command
    quantity = int(input())
    if resource not in resources_dict.keys():
        resources_dict[resource] = 0
    resources_dict[resource] += quantity

    command = input()
for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
