result_first_game = input()
result_second_game = input()
result_third_game = input()
wins = 0
draws = 0
loses = 0
first_num_first_game = int(result_first_game[0])
second_num_first_game = int(result_first_game[2])
first_num_second_game = int(result_second_game[0])
second_num_second_game = int(result_second_game[2])
first_num_third_game = int(result_third_game[0])
second_num_third_game = int(result_third_game[2])
if first_num_first_game > second_num_first_game:
    wins += 1
elif first_num_first_game < second_num_first_game:
    loses += 1
elif first_num_first_game == second_num_first_game:
    draws += 1
if first_num_second_game > second_num_second_game:
    wins += 1
elif first_num_second_game < second_num_second_game:
    loses += 1
elif first_num_second_game == second_num_second_game:
    draws += 1
if first_num_third_game > second_num_third_game:
    wins += 1
elif first_num_third_game < second_num_third_game:
    loses += 1
elif first_num_third_game == second_num_third_game:
    draws += 1
print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")