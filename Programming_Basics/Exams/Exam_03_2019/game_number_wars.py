first_player = input()
second_player = input()
points_first_player = 0
points_second_player = 0
winner = ""
winner_points = 0
is_game_of_wars = False

command = input()
while command != "End of game":
    card_first_player = int(command)
    card_second_player = int(input())
    if card_first_player > card_second_player:
        points_first_player += card_first_player - card_second_player
    elif card_second_player > card_first_player:
        points_second_player += card_second_player - card_first_player
    else:
        print("Number wars!")
        additional_card_first_player = int(input())
        additional_card_second_player = int(input())
        if additional_card_first_player > additional_card_second_player:
            winner = first_player
            winner_points = points_first_player
        else:
            winner = second_player
            winner_points = points_second_player
        is_game_of_wars = True
        break
    command = input()

if is_game_of_wars:
    print(f"{winner} is winner with {winner_points} points")
else:
    print(f"{first_player} has {points_first_player} points")
    print(f"{second_player} has {points_second_player} points")