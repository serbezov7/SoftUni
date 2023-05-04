size = int(input())

matrix = []
for row in range(size):
    current_row = list(input())
    matrix.append(current_row)

directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
)

knights_out = 0
knight_coordinates = [0, 0]
while True:
    max_attacks = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                current_attacks = 0
                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]
                    if 0 <= r < size and 0 <= c < size and matrix[r][c] == "K":
                        current_attacks += 1
                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_coordinates = row, col
    if not max_attacks:
        break
    matrix[knight_coordinates[0]][knight_coordinates[1]] = "0"
    knights_out += 1
print(knights_out)
