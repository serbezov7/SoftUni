command = input()
best_player = ""
goals = 0
hat_trick = False

while command != "END":
    name_of_the_player = command
    goals_scored = int(input())
    if goals_scored > goals:
        goals = goals_scored
        best_player = name_of_the_player
    if goals >= 3:
        hat_trick = True
    if goals >= 10:
        break
    command = input()
print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")