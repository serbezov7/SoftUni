start_number = int(input())
finish_number = int(input())
magic_number = int(input())
combination = 0

flag = False
for i in range(start_number, finish_number + 1):
    for j in range(start_number, finish_number + 1):
        combination += 1
        if i + j == magic_number:
            flag = True
            print(f"Combination N:{combination} ({i} + {j} = {magic_number})")
            break
    if flag:
        break
if not flag:
    print(f"{combination} combinations - neither equals {magic_number}")