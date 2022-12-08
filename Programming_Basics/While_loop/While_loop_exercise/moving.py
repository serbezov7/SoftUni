width = int(input())
length = int(input())
height = int(input())
total_square = width * length * height
sum_boxes = 0
is_place_full = False

command = input()
while command != "Done":
    command = int(command)
    sum_boxes += command
    if total_square < sum_boxes:
        is_place_full = True
        break
    command = input()
difference = abs(total_square - sum_boxes)
if is_place_full:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")