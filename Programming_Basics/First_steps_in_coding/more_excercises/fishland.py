price_mackerel = float(input())
price_small_fish = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

price_bonito = price_mackerel * 1.6
price_horse_mackerel = price_small_fish * 1.8
price_mussels = mussels_kg * 7.50

total_price = (price_bonito*bonito_kg)+(price_horse_mackerel*horse_mackerel_kg)+price_mussels
print("{:.2f}".format(total_price))
