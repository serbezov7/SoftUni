budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
price_per_bread = flour_price + eggs_price + milk_price
breads_count = 0
eggs_count = 0

while budget >= price_per_bread:
    breads_count += 1
    budget -= price_per_bread
    eggs_count += 3
    if breads_count % 3 == 0:
        eggs_count -= breads_count - 2
print(f"You made {breads_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")
