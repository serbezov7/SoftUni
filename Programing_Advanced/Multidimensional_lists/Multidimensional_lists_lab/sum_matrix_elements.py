rows, cols = [int(x) for x in (input().split(", "))]

matrix = []
total_sum = 0
for row in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)
    total_sum += sum(col)

print(total_sum)
print(matrix)
