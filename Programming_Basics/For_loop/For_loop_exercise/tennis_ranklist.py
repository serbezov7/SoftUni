from math import floor

tournaments = int(input())
initial_points = int(input())
points = 0
total_points = 0
won_tournaments = 0

for tournament in range(tournaments):
    stage = input()
    if stage == "W":
        points += 2000
        total_points = points + initial_points
        won_tournaments += 1
    elif stage == "F":
        points += 1200
        total_points = points + initial_points

    else:
        points += 720
        total_points = points + initial_points

average_points = points / tournaments
percent_win = won_tournaments / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_win:.2f}%")
