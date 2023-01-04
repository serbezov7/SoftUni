n = int(input())

print(" " * n + " | " + " " * n)

for row in range(1, n + 1):
    print(" " * (n - row) + "*" * row + " | " + "*" * row + " " * (n - row))
    