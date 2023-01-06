first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))
is_winner = False
for i in range(len(first_row)):
    for j in range(len(second_row)):
        for k in range(len(third_row)):
            if first_row[0] == second_row[0] == third_row[0] and first_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif first_row[0] == second_row[0] == third_row[0] and first_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif first_row[0] == first_row[1] == first_row[2] and first_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif first_row[0] == first_row[1] == first_row[2] and first_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif first_row[0] == second_row[1] == third_row[2] and first_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif first_row[0] == second_row[1] == third_row[2] and first_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif second_row[0] == second_row[1] == second_row[2] and second_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif second_row[0] == second_row[1] == second_row[2] and second_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif third_row[0] == third_row[1] == third_row[2] and third_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif third_row[0] == third_row[1] == third_row[2] and third_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif third_row[0] == third_row[1] == third_row[2] and third_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif third_row[0] == third_row[1] == third_row[2] and third_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif third_row[0] == second_row[1] == first_row[2] and third_row[0] == 1:
                is_winner = True
                print("First player won")
                break
            elif third_row[0] == second_row[1] == first_row[2] and third_row[0] == 2:
                is_winner = True
                print("Second player won")
                break
            elif first_row[2] == second_row[2] == third_row[2] and first_row[2] == 1:
                is_winner = True
                print("First player won")
                break
            elif first_row[2] == second_row[2] == third_row[2] and first_row[2] == 2:
                is_winner = True
                print("Second player won")
                break
        break
    break
if not is_winner:
    print("Draw!")
