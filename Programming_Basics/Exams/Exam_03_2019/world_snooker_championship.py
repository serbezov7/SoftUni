stage = input()
ticket_kind = input()
count_tickets = int(input())
picture_with_trophy = input()
price = 0
if ticket_kind == "Standard":
    if stage == "Quarter final":
        price = 55.50
    elif stage == "Semi final":
        price = 75.88
    else:
        price = 110.10

elif ticket_kind == "Premium":
    if stage == "Quarter final":
        price = 105.20
    elif stage == "Semi final":
        price = 125.22
    else:
        price = 160.66
else:
    if stage == "Quarter final":
        price = 118.90
    elif stage == "Semi final":
        price = 300.40
    else:
        price = 400
total_price = price * count_tickets
if 2500 < total_price <= 4000:
    total_price *= 0.90
    if picture_with_trophy == "Y":
        total_price += count_tickets * 40
elif total_price > 4000:
    total_price *= 0.75
else:
    if picture_with_trophy == "Y":
        total_price += count_tickets * 40
print(f"{total_price:.2f}")