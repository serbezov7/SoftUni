list_items = input().split("|")
budget = float(input())
bought_items = []
profit = 0

for item in list_items:
    current_item = item.split("->")
    price = float(current_item[1])
    if current_item[0] == "Clothes":
        if price <= 50:
            if budget >= price:
                budget -= price
                new_price = price * 1.40    #new_price = float("{:.2f}".format(price * 1.40))
                bought_items.append(price * 1.40)
                profit += new_price - price
    elif current_item[0] == "Shoes":
        if price <= 35:
            if budget >= price:
                budget -= price
                new_price = price * 1.40
                bought_items.append(new_price)
                profit += new_price - price
    elif current_item[0] == "Accessories":
        if price <= 20.50:
            if budget >= price:
                budget -= price
                new_price = price * 1.40
                bought_items.append(new_price)
                profit += new_price - price
for number in bought_items:
    print(f'{number:.2f}', end=" ")
print()
print(f"Profit: {profit:.2f}")

if budget + sum(bought_items) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
