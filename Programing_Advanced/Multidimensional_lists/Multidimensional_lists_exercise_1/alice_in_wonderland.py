size = int(input())
alice_row = 0
alice_col = 0

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
    if "A" in current_row:
        alice_row = row
        alice_col = matrix[row].index("A")
        matrix[alice_row][alice_col] = "*"

collected_tea_bags = 0

while collected_tea_bags < 10:
    command = input()
    r = directions[command][0] + alice_row
    c = directions[command][1] + alice_col

    if not (0 <= r < size and 0 <= c < size):
        break
    elif matrix[r][c] == "R":
        matrix[r][c] = "*"
        break

    elif matrix[r][c].isdigit():
        collected_tea_bags += int(matrix[r][c])
    matrix[r][c] = "*"
    alice_row = r
    alice_col = c

if collected_tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")
[print(*row) for row in matrix]
