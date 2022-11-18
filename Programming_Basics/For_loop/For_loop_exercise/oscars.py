name_actor = input()
initial_points = float(input())
count_people = int(input())
points = 0
total_points = 0
for people in range(count_people):
    name = input()
    current_points = float(input())
    points = points + len(name) * current_points / 2
    total_points = points + initial_points
    if total_points >= 1250.50:
        break
if total_points >= 1250.50:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.50 - total_points
    print(f"Sorry, {name_actor} you need {difference:.1f} more!")