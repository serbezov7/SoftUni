def get_coordinates(row_, col_):
    directions = (
        (row_ - 1, col_),  # up
        (row_ - 1, col_ - 1),  # up left
        (row_ - 1, col_ + 1),  # up right
        (row_ + 1, col_ - 1),  # down left
        (row_ + 1, col_ + 1),  # down right
        (row_ + 1, col_),  # down
        (row_, col + 1),  # right
        (row_, col - 1),  # left
    )
    for_detonation = []
    for r, c in directions:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] > 0:
            for_detonation.append([r, c])
    return for_detonation


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs_coordinates = [[int(x) for x in coordinate.split(",")] for coordinate in input().split()]

for row, col in bombs_coordinates:
    if matrix[row][col] <= 0:
        continue
    power = matrix[row][col]
    matrix[row][col] = 0
    detonation_list = get_coordinates(row, col)
    for r, c in detonation_list:
        matrix[r][c] -= power

alive_cells = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive_cells.append(matrix[row][col])
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*matrix[row]) for row in range(len(matrix))]
