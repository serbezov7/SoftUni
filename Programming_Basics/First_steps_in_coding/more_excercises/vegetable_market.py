price_veg = float(input())
price_fruits = float(input())
total_kg_veg = int(input())
total_kg_fruits = int(input())

total_price = price_veg * total_kg_veg + price_fruits * total_kg_fruits
total_price_eur = total_price / 1.94
print("{:.2f}".format(total_price_eur))
