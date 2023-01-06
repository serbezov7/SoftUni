list_numbers = list(map(int, input().split()))
middle = len(list_numbers) // 2
left_side = list_numbers[:middle]
right_side = list_numbers[- 1:middle:- 1]

sum_left_side = 0
sum_right_side = 0

for number_left in left_side:
    sum_left_side += number_left
    if number_left == 0:
        sum_left_side *= 0.8

for number_right in right_side:
    sum_right_side += number_right
    if number_right == 0:
        sum_right_side *= 0.8

if sum_left_side < sum_right_side:
    print(f"The winner is left with total time: {sum_left_side:.1f}")
else:
    print(f"The winner is right with total time: {sum_right_side:.1f}")

