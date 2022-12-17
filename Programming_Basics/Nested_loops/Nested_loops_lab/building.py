number_of_floors = int(input())
number_of_rooms = int(input())
letter = ""

for floors in range(number_of_floors, 0, -1):
    for rooms in range(number_of_rooms):
        if floors == number_of_floors:
            letter = "L"
        elif floors % 2 == 0:
            letter = "O"
        else:
            letter = "A"
        print(f"{letter}{floors}{rooms}", end=" ")
    print()

