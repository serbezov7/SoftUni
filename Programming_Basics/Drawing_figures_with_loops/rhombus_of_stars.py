n = int(input())
second_star = n - 1
for row in range(1, 2 * n):
    if row <= n:
        print(" " * (n - row) + "* " * row)
    else:
        print(" " * (row - n) + "* " * second_star)
        second_star -= 1

# n = int(input())
#
# for row in range(1, n + 1):
#     print(" " * (n - row) + "* " * row)
# for row in range(1, n):
#     print(" " * row + "* " * (n - row))