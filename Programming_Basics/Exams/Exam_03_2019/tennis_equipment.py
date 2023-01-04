from math import floor, ceil
tennis_rocket_price = float(input())
count_tennis_rockets = int(input())
count_shoes = int(input())
shoes_price = tennis_rocket_price / 6
tennis_rockets = tennis_rocket_price * count_tennis_rockets
total_shoes_price = shoes_price * count_shoes
all_stuffs = tennis_rockets + total_shoes_price
other_stufFs = all_stuffs * 0.2
total_stuffs = all_stuffs + other_stufFs
for_djokovic = total_stuffs / 8
for_sponsors = total_stuffs * 7 / 8
print(f"Price to be paid by Djokovic {floor(for_djokovic)}")
print(f"Price to be paid by sponsors {ceil(for_sponsors)}")