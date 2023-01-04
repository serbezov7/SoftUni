food = int(input())
food_in_grams = food * 1000
eaten_food = 0

command = input()
while command != "Adopted":
    current_foot_grams = int(command)
    eaten_food += current_foot_grams
    command = input()
difference = abs(food_in_grams - eaten_food)
if eaten_food <= food_in_grams:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")