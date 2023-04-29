def get_player_move(row, col, command):
    directions = {
        "U": [row - 1, col],
        "L": [row, col - 1],
        "R": [row, col + 1],
        "D": [row + 1, col]
    }
    r, c = directions[command]
    return r, c


def is_inside(row, col, rows, cols):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False


def get_children(row, col):
    directions = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]
    ]
    result = []
    for direction in directions:
        result.append(direction)
    return result


rows, cols = [int(x) for x in input().split()]

player_row, player_col = 0, 0
bunnies = set()
new_bunnies = set()

matrix = []
for row in range(rows):
    current_row = list(input())
    matrix.append(current_row)
    for col in range(cols):
        if matrix[row][col] == "P":
            player_row, player_col = row, col
        elif matrix[row][col] == "B":
            bunnies.add(f"{row} {col}")
commands = list(input())
won = False
dead = False

for command in commands:
    next_row, next_col = get_player_move(player_row, player_col, command)
    matrix[player_row][player_col] = "."
    if is_inside(next_row, next_col, rows, cols):
        player_row = next_row
        player_col = next_col
        if matrix[next_row][next_col] == "B":
            dead = True
        else:
            matrix[player_row][player_col] = "P"
    else:
        won = True

    for bunnie in bunnies:
        bunnie_row, bunnie_col = [int(x) for x in bunnie.split()]
        next_possible_children = get_children(bunnie_row, bunnie_col)
        for child in next_possible_children:
            r, c = child
            if is_inside(r, c, rows, cols):
                new_bunnies.add(f"{r} {c}")
                if matrix[r][c] == "P":
                    dead = True
                matrix[r][c] = "B"
        bunnies = new_bunnies.union(bunnies)

    if won or dead:
        break

[print(*matrix[row], sep="") for row in range(len(matrix))]
if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
