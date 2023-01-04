count_of_locations = int(input())

for location in range(count_of_locations):
    expected_gold_per_day = float(input())
    days_for_digging = int(input())
    gold_sum = 0
    for day in range(days_for_digging):
        gold_kilos_per_day = float(input())
        gold_sum += gold_kilos_per_day
    average_gold = gold_sum / days_for_digging
    difference = abs(expected_gold_per_day - average_gold)
    if average_gold >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")