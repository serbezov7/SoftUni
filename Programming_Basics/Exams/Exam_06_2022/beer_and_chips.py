from math import ceil
fan_name = input()
budget = float(input())
count_bottles_beer = int(input())
packages_chips = int(input())
price_one_chips = count_bottles_beer * 1.20 * 0.45
price_chips = ceil(price_one_chips * packages_chips)
price_beer = count_bottles_beer * 1.20
total_sum = price_beer + price_chips
difference = abs(total_sum - budget)
if budget >= total_sum:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")
