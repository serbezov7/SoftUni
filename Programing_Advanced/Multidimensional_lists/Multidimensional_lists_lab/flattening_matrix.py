rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
flat_matrix = [] #[x for row in matrix for x in row]

# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         flat_matrix.append(matrix[row][col])

for row in matrix:
    flat_matrix.extend(row)

print(flat_matrix)
