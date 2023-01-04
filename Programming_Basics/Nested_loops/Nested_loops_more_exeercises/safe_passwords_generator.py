first_end = int(input())
second_end = int(input())
max_passwords = int(input())
combinations = 0
first_start = 35
second_start = 64
flag = False

for A in range(first_start, 55):
    for B in range(second_start, 96):
        for x in range(1, first_end + 1):
            for y in range(1, second_end + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                combinations += 1
                A += 1
                B += 1
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64
                if x == first_end and y == second_end:
                    flag = True
                    break
                if combinations == max_passwords:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break

