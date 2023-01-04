command = input()
all_games = 0
win_games = 0
lost_games = 0

while command != "End of tournaments":
    tournament_name = command
    count_games = 0
    difference = 0
    count_of_games = int(input())
    for game in range(count_of_games):
        count_games += 1
        all_games += 1
        points_team_desi = int(input())
        points_other_team = int(input())
        difference = abs(points_team_desi - points_other_team)
        if points_team_desi > points_other_team:
            win_games += 1
            print(f"Game {count_games} of tournament {tournament_name}: win with {difference} points.")
        else:
            lost_games += 1
            print(f"Game {count_games} of tournament {tournament_name}: lost with {difference} points.")
    command = input()
percent_win = win_games / all_games * 100
percent_lost = lost_games / all_games * 100
print(f"{percent_win:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")