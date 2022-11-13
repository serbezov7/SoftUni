age = int(input())
price_wash_machine = float(input())
price_toy = int(input())
toy_count = 0
sum_money = 0
money = 10
brother = 0
for birthday in range(1, age + 1):
    if birthday % 2 != 0:
        toy_count += 1
    else:
        sum_money = sum_money + money
        money = money + 10
        brother += 1

total_money = sum_money + (toy_count * price_toy - brother)
difference = abs(total_money - price_wash_machine)

if total_money >= price_wash_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
