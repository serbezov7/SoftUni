juniors = int(input())
seniors = int(input())
terrain = input()
price_juniors = 0
price_seniors = 0
participants = juniors + seniors
if terrain == "trail":
    price_juniors = juniors * 5.50
    price_seniors = seniors * 7
elif terrain == "cross-country":
    price_juniors = juniors * 8
    price_seniors = seniors * 9.50
elif terrain == "downhill":
    price_juniors = juniors * 12.25
    price_seniors = seniors * 13.75
else:
    price_juniors = juniors * 20
    price_seniors = seniors * 21.50

total_price = price_juniors + price_seniors

if terrain == "cross-country":
    if participants >= 50:
        total_price = total_price * 0.75
total_price_with_expences = total_price * 0.95
print(f"{total_price_with_expences:.2f}")
