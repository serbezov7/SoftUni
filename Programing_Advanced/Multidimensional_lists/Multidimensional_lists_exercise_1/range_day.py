def shooting(direction):
        row = my_row + directions[direction][0]
        col = my_col + directions[direction][1]

        while True:
            if not (0 <= row < size and 0 <= col < size):
                break

            if matrix[row][col] == "x":
                matrix[row][col] = "."
                return [row, col]

            row += directions[direction][0]
            col += directions[direction][1]


def move(direction, steps):
    row = my_row + (directions[direction][0] * steps)
    col = my_col + (directions[direction][1] * steps)
    if not (0 <= row < size and 0 <= col < size):
        return my_row, my_col
    if matrix[row][col] == "x":
        return my_row, my_col
    return [row, col]


size = 5
my_row = 0
my_col = 0
all_targets_count = 0
shooted_targets = 0
shooted_targets_coordinates = []

matrix = []
for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    if "A" in matrix[row]:
        my_row = row
        my_col = matrix[row].index("A")
    if "x" in matrix[row]:
        all_targets_count += matrix[row].count("x")


count_commands = int(input())

directions = {
    "up": [-1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
}

for _ in range(count_commands):
    command = input().split()
    if command[0] == "shoot":
        targets = shooting(command[1])
        if targets:
            shooted_targets_coordinates.append(targets)
            shooted_targets += 1

        if shooted_targets == all_targets_count:
            print(f"Training completed! All {all_targets_count} targets hit.")
            break
    elif command[0] == "move":
        my_row, my_col = move(command[1], int(command[2]))

else:
    print(f"Training not completed! {all_targets_count - shooted_targets} targets left.")
[print(el) for el in (shooted_targets_coordinates)]




# def shooting(direction):
#     row = my_row + directions[direction][0]
#     col = my_col + directions[direction][1]
#
#     while True:
#         if not (0 <= row < size and 0 <= col < size):
#             break
#
#         if matrix[row][col] == "x":
#             matrix[row][col] = "."
#             return [row, col]
#
#         row += directions[direction][0]
#         col += directions[direction][1]
#
#
# def move(direction, steps):
#     row = my_row + directions[direction][0] * int(steps)
#     col = my_col + directions[direction][1] * int(steps)
#     if not (0 <= row < size and 0 <= col < size):
#         return my_row, my_col
#     if matrix[row][col] == "x":
#         return my_row, my_col
#     return row, col
#
#
# size = 5
# my_row = 0
# my_col = 0
# all_targets_count = 0
# shooted_targets = 0
# shooted_targets_coordinates = []
#
# matrix = []
# for row in range(size):
#     current_row = input().split()
#     matrix.append(current_row)
#     if "A" in matrix[row]:
#         my_row = row
#         my_col = matrix[row].index("A")
#     if "x" in matrix[row]:
#         all_targets_count += matrix[row].count("x")
#
# count_commands = int(input())
#
# directions = {
#     "up": [-1, 0],
#     "left": [0, -1],
#     "right": [0, 1],
#     "down": [1, 0],
# }
#
# for _ in range(count_commands):
#     command = input().split()
#     if command[0] == "shoot":
#         targets = shooting(command[1])
#         if targets:
#             shooted_targets_coordinates.append(targets)
#             shooted_targets += 1
#
#         if shooted_targets == all_targets_count:
#             print(f"Training completed! All {all_targets_count} targets hit.")
#             break
#     elif command[0] == "move":
#         my_row, my_col = move(command[1], command[2])
#
# else:
#     print(f"Training not completed! {all_targets_count - shooted_targets} targets left.")
# [print(el) for el in (shooted_targets_coordinates)]