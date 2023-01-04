from math import  ceil
count_people = int(input())
entrance = float(input())
price_sunbed = float(input())
price_umbrella = float(input())
money_for_umbrella = ceil(count_people / 2) * price_umbrella
money_for_entrance = entrance * count_people
money_sunbeds = ceil(count_people * 0.75) * price_sunbed
all_price = money_for_umbrella + money_for_entrance + money_sunbeds
print(f"{all_price:.2f} lv." )