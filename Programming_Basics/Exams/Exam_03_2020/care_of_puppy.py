food = int(input())
command = input()
total_eaten_food = 0
food_in_grams = food * 1000
is_food_enought = True

while command != "Adopted":
    eaten_food = int(command)
    total_eaten_food += eaten_food
    command = input()
difference = abs(food_in_grams - total_eaten_food)
if total_eaten_food <= food_in_grams:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")