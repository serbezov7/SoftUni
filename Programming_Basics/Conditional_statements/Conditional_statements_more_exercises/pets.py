from math import floor,ceil

days = int(input())
food_kg = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input())

total_food = (food_per_day_dog * days) + (food_per_day_cat * days) +(food_per_day_turtle / 1000 * days)
difference = abs(food_kg - total_food)
if total_food <= food_kg:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")

