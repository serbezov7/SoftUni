number_of_snowballs = int(input())
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0

for ball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time = int(input())
    quality = int(input())
    value_of_snowball = (weight_of_snowball / time) ** quality
    if value_of_snowball > best_snowball_value:
        best_snowball_weight = weight_of_snowball
        best_snowball_time = time
        best_snowball_quality = quality
        best_snowball_value = value_of_snowball
print(f"{best_snowball_weight} : {best_snowball_time} = {int(best_snowball_value)} ({best_snowball_quality})")

