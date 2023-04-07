rows, cols = [int(x) for x in input().split()]
first_letter = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(row + first_letter)}{chr(row + first_letter + col)}{chr(row + first_letter)}", end=" ")
    print()
