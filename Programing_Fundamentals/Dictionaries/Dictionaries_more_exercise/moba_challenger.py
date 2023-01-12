command = input()
players_dict = {}

while command != "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players_dict.keys():
            players_dict[player] = {position: skill}
        else:
            for positions in players_dict[player].keys():
                if positions == position:
                    if players_dict[player][positions] < skill:
                        players_dict[player][positions] += skill
                    break
            else:
                players_dict[player][position] = skill
    else:
        first_player, second_player = command.split(" vs ")
        is_demoted = False
        if first_player in players_dict.keys() and second_player in players_dict.keys():
            for first_player_pos in players_dict[first_player]:
                for second_player_pos in players_dict[second_player]:
                    if first_player_pos == second_player_pos:
                        if players_dict[first_player][first_player_pos] > players_dict[second_player][second_player_pos]:
                            del players_dict[second_player]
                            is_demoted = True
                            break
                        elif players_dict[first_player][first_player_pos] < players_dict[second_player][second_player_pos]:
                            del players_dict[first_player]
                            is_demoted = True
                            break
                        else:
                            continue
                if is_demoted:
                    break

    command = input()
skill_dict = {}
for current_player in players_dict.keys():
    total_skill = 0
    for points in players_dict[current_player].values():
        total_skill += points
    skill_dict[current_player] = total_skill
for player, total_skill in sorted(skill_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {total_skill} skill")
    for location, skill in sorted(players_dict[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {location} <::> {skill}")
