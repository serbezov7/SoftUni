rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
while True:
    commands = [int(x) if x.lstrip("-").isdigit() else x for x in input().split()]
    if len(commands) > 1:
        action, row, col, value = commands
        if 0 <= row < rows and 0 <= col < rows:
            if action == "Add":
                matrix[row][col] += value
            elif action == "Subtract":
                matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    else:
        break

[print(*row)for row in matrix]
