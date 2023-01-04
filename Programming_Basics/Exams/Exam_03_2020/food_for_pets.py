days = int(input())
total_food = float(input())
eaten_food = 0
eaten_by_dog = 0
eaten_by_cat = 0
biscuits = 0
eaten_third_day_cat = 0
eaten_third_day_dog = 0

for day in range(1, days + 1):
    food_eaten_dog = int(input())
    eaten_by_dog += food_eaten_dog
    eaten_food += food_eaten_dog
    eaten_third_day_dog = food_eaten_dog
    food_eaten_cat = int(input())
    eaten_by_cat += food_eaten_cat
    eaten_food += food_eaten_cat
    eaten_third_day_cat = food_eaten_cat
    if day % 3 == 0 and day != 0:
        eaten_third_day = eaten_third_day_cat + eaten_third_day_dog
        biscuits += (eaten_third_day * 0.1)
biscuits = round(biscuits)
percent_dog = eaten_by_dog / eaten_food * 100
percent_cat = eaten_by_cat / eaten_food * 100
total_percent = eaten_food / total_food * 100

print(f"Total eaten biscuits: {biscuits}gr.")
print(f"{total_percent:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")

