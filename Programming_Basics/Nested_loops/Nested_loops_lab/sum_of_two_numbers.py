starting_number = int(input())
final_number = int(input())
magic_number = int(input())
combination = 0
is_combination_found = False

for first_number in range(starting_number, final_number + 1):
    for second_number in range(starting_number, final_number + 1):
        combination += 1
        if first_number + second_number == magic_number:
            is_combination_found = True
            break
    if is_combination_found:
        break
if is_combination_found:
    print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")