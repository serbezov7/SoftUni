budget = float(input())
statists = int(input())
clothes_price_one = float(input())

decor = budget * 0.1
clothes_sum = statists * clothes_price_one

if statists >= 150:
    clothes_sum = clothes_sum * 0.9
expences = decor + clothes_sum
money_left = abs(budget - expences)

if budget >= expences:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")