def print_rhombus(size):

    for row in range(1, size + 1):
        stars = row
        empty_spaces = size - row
        print(" " * empty_spaces + "* " * stars)
    for row in range(1, size):
        stars = size - row
        empty_spaces = row
        print(" " * empty_spaces + "* " * stars)


size = int(input())
print_rhombus(size)

# def print_rhombus(size):
#
#     for row in range(size, 0, -1):
#         stars = size - row + 1
#         empty_spaces = row - 1
#         print(" " * empty_spaces + "* " * stars)
#     for row in range(size, 1, -1):
#         stars = row - 1
#         empty_spaces = size - row + 1
#         print(" " * empty_spaces + "* " * stars)
#
#
# size = int(input())
# print_rhombus(size)