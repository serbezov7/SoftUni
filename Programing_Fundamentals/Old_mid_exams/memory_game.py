elements = input().split()
command = input().split()
moves = 0
is_elements_empty = False


while command[0] != "end":
    elements_copy = elements.copy()
    first_index = int(command[0])
    second_index = int(command[1])
    middle = len(elements) // 2
    moves += 1
    if first_index not in range(len(elements)) or second_index not in range(len(elements))\
            or first_index == second_index:
        print("Invalid input! Adding additional elements to the board")
        elements_copy.insert(middle, f"-{moves}a")
        elements_copy.insert(middle, f"-{moves}a")
    else:
        if elements[first_index] == elements[second_index]:
            print(f"Congrats! You have found matching elements - {elements[first_index]}!")
            elements_copy.remove(elements[first_index])
            elements_copy.remove(elements[second_index])
        elif elements[first_index] != elements[second_index]:
            print("Try again!")
    if len(elements_copy) <= 0:
        is_elements_empty = True
        break
    elements = elements_copy
    command = input().split()

if is_elements_empty:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
    