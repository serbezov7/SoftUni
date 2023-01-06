team_a = ["A-" + str(x) for x in range(1, 12)]
team_b = ["B-" + str(x) for x in range(1, 12)]

game_was_terminated = False
players_off = input().split()
for player in players_off:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")
