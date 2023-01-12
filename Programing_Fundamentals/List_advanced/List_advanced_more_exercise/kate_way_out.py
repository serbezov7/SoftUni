matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    matrix.append([x for x in input()])

kate_position = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "k":
            kate_position = row, col
kate_row = kate_position[0]
kate_col = kate_position[1]
is_won = False
while True:
    if kate_row + 1 > len(matrix) - 1 or kate_row - 1 < 0 or kate_col + 1 > len(matrix[0]) - 1 or kate_col - 1 < 0:
        is_won = True
        break
    if matrix[kate_row + 1][kate_col] != " " and matrix[kate_row - 1][kate_col] != " " and \
            matrix[kate_row][kate_col + 1] != " " and matrix[kate_row][kate_col - 1] != " ":
        print("Kate cannot get out")
        break

        # going up
    if matrix[kate_row - 1][kate_col] == " ":
        matrix[kate_row - 1][kate_col] = "k"
        kate_row = kate_row - 1
        # going down
    elif matrix[kate_row + 1][kate_col] == " ":
        matrix[kate_row + 1][kate_col] = "k"
        kate_row = kate_row + 1
        # going right
    elif matrix[kate_row][kate_col + 1] == " ":
        matrix[kate_row][kate_col + 1] = "k"
        kate_col = kate_col + 1
        # going left
    elif matrix[kate_row][kate_col - 1] == " ":
        matrix[kate_row][kate_col - 1] = "k"
        kate_col = kate_col - 1

if is_won:
    counter = 0
    for el in matrix:
        counter += el.count("k")
        counter += el.count(" ")
    print(f"Kate got out in {counter} moves")



# def find_Kate(mx):
#     for i in range(len(mx)):
#         for j in range(len(mx[i])):
#             if mx[i][j] == 'k':
#                 return i, j
#
#
# def move_Kate(mx, directions, moves=[], count=0):
#     while True:
#         position = find_Kate(mx)
#         if position is None:
#             if not moves:
#                 return 'Kate cannot get out'
#             else:
#                 return min(moves)
#         else:
#             r, c = position
#         mx[r][c] = '$'
#         for direction in directions:
#             if r + directions[direction][0] < len(mx) and 0 <= c + directions[direction][1] < len(mx[r]):
#                 if mx[r + directions[direction][0]][c + directions[direction][1]] == ' ':
#                     mx[r + directions[direction][0]][c + directions[direction][1]] = 'k'
#                     move_Kate(mx, directions, moves, count + 1)
#             else:
#                 count += 1
#                 moves.append(count)
#
#
# maze = [list(input()) for _ in range(int(input()))]
# movement = {
#     'U': [-1, 0],
#     'D': [1, 0],
#     'R': [0, 1],
#     'L': [0, -1],
# }
# res = move_Kate(maze, movement)
# if str(res).isdigit():
#     print(f'Kate got out in {res} moves')
# else:
#     print(res)
