budget = float(input())
category = input()
people = int(input())
money_left = 0
total_price_VIP = people * 499.99
total_price_normal = people * 249.99

if people <= 4:
    money_left = budget * 0.25
elif people <= 9:
    money_left = budget * 0.4
elif people <= 24:
    money_left = budget * 0.5
elif people <= 49:
    money_left = budget * 0.6
else:
    money_left = budget * 0.75

if category == "VIP":
    if money_left >= total_price_VIP:
        difference = abs(money_left - total_price_VIP)
        print(f"Yes! You have {difference:.2f} leva left.")
    else:
        difference = abs(money_left - total_price_VIP)
        print(f"Not enough money! You need {difference:.2f} leva.")
else:
    if money_left >= total_price_normal:
        difference = abs(money_left - total_price_normal)
        print(f"Yes! You have {difference:.2f} leva left.")
    else:
        difference = abs(money_left - total_price_normal)
        print(f"Not enough money! You need {difference:.2f} leva.")


