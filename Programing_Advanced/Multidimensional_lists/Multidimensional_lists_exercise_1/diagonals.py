size = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(size)]
primary = [matrix[i][i] for i in range(size)]
secondary = [matrix[size - i - 1][i] for i in range(size - 1, -1, -1)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
