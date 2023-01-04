from math import ceil

height = int(input())
width = int(input())
percent_not_painted = int(input())
all_walls = height * width * 4
for_painting = ceil(all_walls - (all_walls * percent_not_painted / 100))
painted = 0
difference = 0
is_all_painted = False

command = input()
while command != "Tired!":
    painted_area = int(command)
    painted += painted_area
    if painted >= for_painting:
        is_all_painted = True
        break
    command = input()
difference = abs(for_painting - painted)
if is_all_painted:
    if difference == 0:
        print(f"All walls are painted! Great job, Pesho!")
    else:
        print(f"All walls are painted and you have {difference} l paint left!")
else:
    print(f"{difference} quadratic m left.")

