size = int(input())
bunny_row = 0
bunny_col = 0

directions = {
    "up": [-1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
}

matrix = []
for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    if "B" in current_row:
        bunny_row, bunny_col = row, matrix[row].index("B")

profit_position = ""
profit_path = []
best_sum = 0

for direction in directions:
    current_sum = 0
    current_path = []
    r = bunny_row + directions[direction][0]
    c = bunny_col + directions[direction][1]
    while 0 <= r < size and 0 <= c < size and matrix[r][c] != "X":
        current_path.append([r, c])
        current_sum += int(matrix[r][c])
        r += directions[direction][0]
        c += directions[direction][1]
    if current_sum >= best_sum:
        best_sum = current_sum
        profit_path = current_path
        profit_position = direction

print(profit_position)
[print(row) for row in profit_path]
print(best_sum)
