distance = int(input())
tariff = input()
price = 0
if tariff == "day":
    taxi_price = 0.79
else:
    taxi_price = 0.90
if distance < 20:
    price = (distance * taxi_price) + 0.70
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06
print(f"{price:.2f}")

