command = input()
my_dict = {}

while command != "statistics":
    key, value = command.split(": ")
    if key not in my_dict.keys():
        my_dict[key] = 0
    my_dict[key] += int(value)

    command = input()
print("Products in stock:")
for product in my_dict.keys():
    print(f"- {product}: {my_dict[product]}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
