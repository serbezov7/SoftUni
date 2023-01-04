minutes_walking = int(input())
count_walks = int(input())
calories = int(input())
enough_calories = calories / 2

total_minutes = minutes_walking * count_walks
burned_calories = total_minutes * 5
if burned_calories >= enough_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")