number = int(input())
current_num = 0
is_number_bigger = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        current_num += 1
        if current_num > number:
            is_number_bigger = True
            break
        print(current_num, end=" ")
    if is_number_bigger:
        break
    print()