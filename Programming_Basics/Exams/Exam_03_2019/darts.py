player_name = input()
initial_points = 301
starting_points = initial_points
successful_shot = 0
unsuccessful_shot = 0
are_points_zero = False

command = input()
while command != "Retire":
    area = command
    points = int(input())
    if area == "Single":
        initial_points -= points
    elif area == "Double":
        initial_points -= points * 2
    else:
        initial_points -= points * 3
    if initial_points < 0:
        unsuccessful_shot += 1
        initial_points = starting_points
    elif initial_points > 0:
        successful_shot += 1
        starting_points = initial_points
    else:
        successful_shot += 1
        are_points_zero = True
        break
    command = input()
if are_points_zero:
    print(f"{player_name} won the leg with {successful_shot} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shot} unsuccessful shots.")