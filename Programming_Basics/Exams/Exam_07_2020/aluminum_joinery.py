count_joinery = int(input())
kind_joinery = input()
delivery = input()
price = 0

if kind_joinery == "90X130":
    price = count_joinery * 110
    if 30 < count_joinery <= 60:
        price *= 0.95
    elif count_joinery > 60:
        price *= 0.92
elif kind_joinery == "100X150":
    price = count_joinery * 140
    if 40 < count_joinery <= 80:
        price *= 0.94
    elif count_joinery > 80:
        price *= 0.9
elif kind_joinery == "130X180":
    price = count_joinery * 190
    if 20 < count_joinery <= 50:
        price *= 0.93
    elif count_joinery > 50:
        price *= 0.88
else:
    price = count_joinery * 250
    if 25 < count_joinery <= 50:
        price *= 0.91
    elif count_joinery > 50:
        price *= 0.86
if delivery == "With delivery":
    price += 60
if count_joinery > 99:
    price *= 0.96
if count_joinery < 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")