from math import ceil
n = int(input())

print("*" * n * 2 + " " * n + "*" * n * 2)

for row in range(1, n - 1):
    if row == ceil(n / 2 - 1):
        print("*" + "/" * (n * 2 - 2) + "*" + "|" * n + "*" + "/" * (n * 2 - 2) + "*")
    else:
        print("*" + "/" * (n * 2 - 2) + "*" + " " * n + "*" + "/" * (n * 2 - 2) + "*")

print("*" * n * 2 + " " * n + "*" * n * 2)
