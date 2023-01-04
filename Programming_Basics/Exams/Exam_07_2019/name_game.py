import sys
command = input()
max_score = -sys.maxsize
winner_name = ""

while command != "Stop":
    name_of_the_player = command
    current_result = 0

    for letter in name_of_the_player:
        current_num = int(input())
        if current_num == ord(letter):
            current_result += 10
        else:
            current_result += 2
    if current_result >= max_score:
        max_score = current_result
        winner_name = name_of_the_player
    command = input()
print(f"The winner is {winner_name} with {max_score} points!")