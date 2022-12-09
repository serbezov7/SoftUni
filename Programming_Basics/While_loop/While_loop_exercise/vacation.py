needed_money = float(input())
initial_money = float(input())
money_saved = initial_money
days_spend = 0
days = 0
five_days_spend = False

while money_saved < needed_money:
    command = input()
    current_sum = float(input())
    days += 1
    if command == "spend":
        money_saved -= current_sum
        days_spend += 1
        if money_saved < 0:
            money_saved = 0
        if days_spend == 5:
            five_days_spend = True
            break
    else:
        money_saved += current_sum
        days_spend = 0

if five_days_spend:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")