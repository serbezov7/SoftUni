needed_profit = float(input())
command = input()
price = 0
total_sum = 0
total_price = 0
is_sum_enought = False

while command != "Party!":
    cocktail_name = command
    cocktails_count = int(input())
    price = len(cocktail_name)
    total_price = price * cocktails_count
    if total_price % 2 != 0:
        total_price *= 0.75
    total_sum += total_price
    if total_sum >= needed_profit:
        is_sum_enought = True
        break
    command = input()
if is_sum_enought:
    print("Target acquired.")
else:
    difference = abs(needed_profit - total_sum)
    print(f"We need {difference:.2f} leva more.")
print(f"Club income - {total_sum:.2f} leva.")