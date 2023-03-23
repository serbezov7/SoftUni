rows = int(input())

matrix = []
diagonal_sum = 0

for row in range(rows):
    col = [int(x) for x in input().split()]
    matrix.append(col)

for idx in range(rows):
    diagonal_sum += matrix[idx][idx]

print(diagonal_sum)
