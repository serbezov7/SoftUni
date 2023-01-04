from math import ceil, floor

count_tournaments = int(input())
initial_points = int(input())
current_points = 0
wins = 0

for tournament in range(count_tournaments):
    stage = input()
    if stage == "W":
        wins += 1
        current_points += 2000
    elif stage == "F":
        current_points += 1200
    else:
        current_points += 720
average = current_points / count_tournaments
average_wins = wins / count_tournaments * 100
all_points = initial_points + current_points
print(f"Final points: {all_points}")
print(f"Average points: {floor(average)}")
print(f"{average_wins:.2f}%")