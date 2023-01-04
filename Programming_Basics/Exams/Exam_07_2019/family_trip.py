budget = float(input())
nights = int(input())
price_for_night = float(input())
percent_add_costs = float(input())
if nights > 7:
    price_for_night *= 0.95
price_for_nights = nights * price_for_night
add_costs = budget * percent_add_costs / 100
total_price = price_for_nights + add_costs
difference = abs(total_price - budget)
if budget >= total_price:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")