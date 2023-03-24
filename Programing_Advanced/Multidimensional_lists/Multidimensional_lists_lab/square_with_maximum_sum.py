rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)
maximum_sum = 0
numbers = []
for row in range(rows - 1):
    for col in range(len(matrix[row]) - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > maximum_sum:
            numbers = []
            maximum_sum = current_sum
            numbers.append([matrix[row][col], matrix[row][col + 1]])
            numbers.append([matrix[row + 1][col], matrix[row + 1][col + 1]])

for row in range(len(numbers)):
    for num in numbers[row]:
        print(num, end=" ")
    print()
print(maximum_sum)
