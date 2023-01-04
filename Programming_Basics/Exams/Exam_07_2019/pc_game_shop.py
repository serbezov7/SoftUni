number_sold_games = int(input())
count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others = 0
count_all = 0
for game in range(number_sold_games):
    current_game = input()
    if current_game == "Hearthstone":
        count_hearthstone += 1
        count_all += 1
    elif current_game == "Fornite":
        count_fornite += 1
        count_all += 1
    elif current_game == "Overwatch":
        count_overwatch += 1
        count_all += 1
    else:
        count_others += 1
        count_all += 1
percent_hearthstone = count_hearthstone / count_all * 100
percent_fornite = count_fornite / count_all * 100
percent_overwatch = count_overwatch / count_all * 100
percent_others = count_others / count_all * 100
print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")