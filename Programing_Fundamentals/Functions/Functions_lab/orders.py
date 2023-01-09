def order(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1
    elif product == "snacks":
        price = 2
    return "{:.2f}".format(price * quantity)


current_product = input()
current_quantity = int(input())
print(order(current_product, current_quantity))
