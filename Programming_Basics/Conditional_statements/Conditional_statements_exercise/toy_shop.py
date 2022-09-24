trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toy_price = (puzzles * 2.60) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)
total_num_toys = puzzles + dolls + bears + minions + trucks

if total_num_toys >= 50:
    total_toy_price = total_toy_price * 0.75

rent = total_toy_price * 0.1
profit = total_toy_price - rent
rest_money = abs(profit - trip)
if profit >= trip:
    print(f"Yes! {rest_money:.2f} lv left.")
else:
    print(f"Not enough money! {rest_money:.2f} lv needed.")
