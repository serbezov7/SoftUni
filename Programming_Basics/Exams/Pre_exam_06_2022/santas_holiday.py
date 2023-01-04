days_stay = int(input())
room_kind = input()
value = input()
price = 0
if room_kind == "president apartment":
    if days_stay < 10:
        price = 35 * 0.9
    elif days_stay <= 15:
        price = 35 * 0.85
    else:
        price = 35 * 0.8
elif room_kind == "apartment":
    if days_stay < 10:
        price = 25 * 0.7
    elif days_stay <= 15:
        price = 25 * 0.65
    else:
        price = 25 * 0.5
else:
    price = 18
total_price = price * (days_stay - 1)
if value == "positive":
    total_price *= 1.25
else:
    total_price *= 0.9
print(f"{total_price:.2f}")

