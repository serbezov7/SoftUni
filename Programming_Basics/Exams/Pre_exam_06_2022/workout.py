from math import ceil
days_training = int(input())
current_distance = float(input())
total_distance = 0
starting_day = current_distance

for day in range(days_training):

    increase_percent = float(input())
    current_distance += (current_distance * increase_percent / 100)
    total_distance += current_distance
total_distance += starting_day
difference = abs(total_distance - 1000)
if total_distance >= 1000:
    print(f"You've done a great job running {ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(difference)} more kilometers")