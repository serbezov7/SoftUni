from math import ceil, floor
n = int(input())
dash = floor(n / 2)
underline = n * 2 - ((dash * 2) + 4)
upperline = n * 2 - 2 * (dash + 1) - 2

print("/" + "^" * dash + "\\" + "_" * underline + "/" + "^" * dash + "\\")

for row in range(1, n - 1):
    if row == n - 2:
        print("|" + " " * (dash + 1) + "_" * upperline + " " * (dash + 1) + "|")
    else:
        print("|" + " " * (2 * n - 2) + "|")
print("\\" + "_" * dash + "/" + " " * underline + "\\" + "_" * dash + "/")

