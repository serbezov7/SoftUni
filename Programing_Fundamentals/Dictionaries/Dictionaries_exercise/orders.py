command = input()
products_dict = {}
new_products = products_dict.copy()
while command != "buy":
    current_command = command.split()
    name = current_command[0]
    price = float(current_command[1])
    quantity = float(current_command[2])

    if name not in products_dict.keys():
        products_dict[name] = quantity
        new_products[name] = quantity * price

    else:
        products_dict[name] += quantity
        new_products[name] = products_dict[name] * price

    command = input()
for product, total_price in new_products.items():
    print(f"{product} -> {total_price:.2f}")
    