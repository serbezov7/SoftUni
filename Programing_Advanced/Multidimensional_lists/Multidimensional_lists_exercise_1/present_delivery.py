def eat_cookie(nice_kids_gifted_, total_presents_):
    for direction in directions.keys():
        r = santa_row + directions[direction][0]
        c = santa_col + directions[direction][1]
        if 0 <= r < size and 0 <= c < size:
            if matrix[r][c] == "V":
                nice_kids_gifted_ += 1
                total_presents_ -= 1
            elif matrix[r][c] == "X":
                total_presents_ -= 1
        matrix[r][c] = "-"
        if not total_presents_:
            break
    return nice_kids_gifted_, total_presents_


total_presents = int(input())
size = int(input())
santa_row = 0
santa_col = 0
total_nice_kids = 0
nice_kids_gifted = 0

matrix = []
for row in range(size):
    current_row = input().split()
    matrix.append(current_row)
    if "S" in matrix[row]:
        santa_row = row
        santa_col = matrix[row].index("S")
    if "V" in matrix[row]:
        total_nice_kids += matrix[row].count("V")

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

command = input()
while command != "Christmas morning":
    matrix[santa_row][santa_col] = "-"
    row = santa_row + directions[command][0]
    col = santa_col + directions[command][1]

    if 0 <= row < size and 0 <= col < size:
        santa_row = row
        santa_col = col
        if matrix[row][col] == "V":
            nice_kids_gifted += 1
            total_presents -= 1
        elif matrix[row][col] == "C":
            nice_kids_gifted, total_presents = eat_cookie(nice_kids_gifted, total_presents)

        matrix[row][col] = "S"
        if not total_presents:
            break

    command = input()

if total_nice_kids - nice_kids_gifted > 0 and not total_presents:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if total_nice_kids - nice_kids_gifted == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_gifted} nice kid/s.")
