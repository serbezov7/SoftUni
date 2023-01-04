football_team = input()
played_games = int(input())
wins = 0
draws = 0
loses = 0
all_matches = 0
all_points = 0
percent_win = 0
if played_games == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    for game in range(played_games):
        result_of_the_game = input()
        if result_of_the_game == "W":
            wins += 1
            all_matches += 1
            all_points += 3
        elif result_of_the_game == "D":
            draws += 1
            all_matches += 1
            all_points += 1
        else:
            loses += 1
            all_matches += 1
    percent_win = wins / all_matches * 100
    print(f"{football_team} has won {all_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {percent_win:.2f}%")