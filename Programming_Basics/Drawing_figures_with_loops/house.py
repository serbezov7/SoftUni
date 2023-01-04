from math import ceil, floor
n = int(input())

if n % 2 == 0:
    spaces = ceil((n - 2) / 2)
    stars = 2
    for row in range(1, (ceil(n / 2) + 1)):
        print("-" * spaces + "*" * stars + "-" * spaces)
        spaces -= 1
        stars += 2
    for row in range(1, floor(n / 2) + 1):
        print("|" + "*" * (n - 2) + "|")
else:
    spaces = ceil((n - 2) / 2)
    stars = 1
    for row in range(1, (ceil(n / 2) + 1)):
        print("-" * spaces + "*" * stars + "-" * spaces)
        spaces -= 1
        stars += 2
    for row in range(1, floor(n / 2) + 1):
        print("|" + "*" * (n - 2) + "|")
