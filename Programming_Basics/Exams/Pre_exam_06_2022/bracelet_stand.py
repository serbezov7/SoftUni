daily_money = float(input())
earn_money_per_day = float(input())
expenses = float(input())
gift_price = float(input())
saved_daily = 5 * daily_money
saved_earn_money = 5 * earn_money_per_day
all_money = saved_daily + saved_earn_money
left_money = all_money - expenses
if left_money >= gift_price:
    print(f"Profit: {left_money:.2f} BGN, the gift has been purchased.")
else:
    difference = gift_price - left_money
    print(f"Insufficient money: {difference:.2f} BGN.")