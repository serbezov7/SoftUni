def check_validation(command_, coordinates_):
    if len(coordinates_) != 4 or command_ != "swap" or not 0 <= coordinates_[0] < rows or not \
            0 <= coordinates_[1] < cols or not 0 <= coordinates_[2] < rows or not \
            0 <= coordinates_[3] < cols:
        return False
    return True


def swap_func():
    if check_validation(command, coordinates):
        matrix[coordinates[0]][coordinates[1]], matrix[coordinates[2]][coordinates[3]] = \
            matrix[coordinates[2]][coordinates[3]], matrix[coordinates[0]][coordinates[1]]
        [print(*matrix[row]) for row in range(len(matrix))]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]
    if command == "END":
        break
    swap_func()
