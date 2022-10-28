days_stay = int(input())
room = input()
opinion = input()
price = 0

if room == "apartment":
    if days_stay < 10:
        price = (days_stay - 1) * 25 * 0.7
    elif days_stay < 15:
        price = (days_stay - 1) * 25 * 0.65
    else:
        price = (days_stay - 1) * 25 * 0.5
elif room == "president apartment":
    if days_stay < 10:
        price = (days_stay - 1) * 35 * 0.9
    elif days_stay < 15:
        price = (days_stay - 1) * 35 * 0.85
    else:
        price = (days_stay - 1) * 35 * 0.8
else:
    price = (days_stay - 1) * 18

if opinion == "positive":
    price = price * 1.25
else:
    price = price * 0.9
print(f"{price:.2f}")

