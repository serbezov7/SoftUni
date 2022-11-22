stadium_capacity = int(input())
count_all_fans = int(input())
fans_in_a = 0
fans_in_b = 0
fans_in_v = 0
fans_in_g = 0

for fan in range(count_all_fans):
    sector = input()
    if sector == "A":
        fans_in_a += 1
    elif sector == "B":
        fans_in_b += 1
    elif sector == "V":
        fans_in_v += 1
    else:
        fans_in_g += 1
percent_a = fans_in_a / count_all_fans * 100
percent_b = fans_in_b / count_all_fans * 100
percent_v = fans_in_v / count_all_fans * 100
percent_g = fans_in_g / count_all_fans * 100
percent_all = count_all_fans / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_all:.2f}%")