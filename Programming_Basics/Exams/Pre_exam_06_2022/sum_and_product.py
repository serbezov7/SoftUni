number = int(input())
valid_combination = False

for a in range(1, 9 + 1):
    for b in range(9, a - 1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                if a + b + c + d == a * b * c * d and number % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    valid_combination = True
                    break
                elif a * b * c * d // (a + b + c + d) == 3 and number % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    valid_combination = True
                    break
            if valid_combination:
                break
        if valid_combination:
            break
    if valid_combination:
        break
if not valid_combination:
    print("Nothing found")