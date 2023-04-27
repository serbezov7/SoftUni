def get_direction(row, col, command):
    directions = {
        "up": [row - 1, col],
        "right": [row, col + 1],
        "left": [row, col - 1],
        "down": [row + 1, col],
    }
    r, c = directions[command]
    return r, c


size = int(input())
commands = input().split()

miner_row = 0
miner_col = 0
number_of_coals = 0
collected_coals = 0
matrix = []

for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(len(matrix[row])):
        if matrix[row][col] == "s":
            miner_row = row
            miner_col = col
        elif matrix[row][col] == "c":
            number_of_coals += 1
for command in commands:
    next_row, next_col = get_direction(miner_row, miner_col, command)
    if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix):
        continue
    matrix[miner_row][miner_col] = "*"
    miner_row = next_row
    miner_col = next_col
    if matrix[miner_row][miner_col] == "c":
        collected_coals += 1
        if collected_coals == number_of_coals:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break
    elif matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        break
else:
    print(f"{number_of_coals - collected_coals} pieces of coal left. ({miner_row}, {miner_col})")
    