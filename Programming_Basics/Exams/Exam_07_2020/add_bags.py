price_luggage_over_20_kg = float(input())
luggage_kilos = float(input())
days_left = int(input())
count_luggage = int(input())
price = 0
if luggage_kilos < 10:
    price = price_luggage_over_20_kg * 0.2
elif luggage_kilos <= 20:
    price = price_luggage_over_20_kg * 0.5
else:
    price = price_luggage_over_20_kg
if days_left < 7:
    price *= 1.40
elif days_left <= 30:
    price *= 1.15
else:
    price *= 1.10
all_price = price * count_luggage

print(f"The total price of bags is: {all_price:.2f} lv.")