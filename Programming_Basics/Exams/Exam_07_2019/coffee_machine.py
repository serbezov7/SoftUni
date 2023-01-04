drink = input()
sugar_level = input()
count_drinks = int(input())
price = 0

if drink == "Espresso":
    if sugar_level == "Without":
        price = count_drinks * 0.90
    elif sugar_level == "Normal":
        price = count_drinks * 1
    else:
        price = count_drinks * 1.20
elif drink == "Cappuccino":
    if sugar_level == "Without":
        price = count_drinks * 1
    elif sugar_level == "Normal":
        price = count_drinks * 1.20
    else:
        price = count_drinks * 1.60
else:
    if sugar_level == "Without":
        price = count_drinks * 0.50
    elif sugar_level == "Normal":
        price = count_drinks * 0.60
    else:
        price = count_drinks * 0.70
if sugar_level == "Without":
    price *= 0.65
if drink == "Espresso" and count_drinks >= 5:
    price *= 0.75
if price > 15:
    price *= 0.80
print(f"You bought {count_drinks} cups of {drink} for {price:.2f} lv.")