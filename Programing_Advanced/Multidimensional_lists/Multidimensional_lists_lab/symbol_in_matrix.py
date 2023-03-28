rows = int(input())

matrix = []

for row in range(rows):
    col = input()
    matrix.append(col)

searched_symbol = input()
is_found = False

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            print(f"({row}, {col})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{searched_symbol} does not occur in the matrix")
