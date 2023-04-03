size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
primary = sum([matrix[i][i] for i in range(size)])
secondary = sum([matrix[size - i - 1][i] for i in range(size - 1, -1, -1)])

print(abs(primary - secondary))
