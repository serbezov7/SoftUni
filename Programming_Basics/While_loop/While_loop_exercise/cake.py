width = int(input())
length = int(input())
all_pieces = width * length
pieces_count = 0
command = input()
while command != "STOP":
    pieces = int(command)
    pieces_count += pieces
    all_pieces -= pieces
    if all_pieces < 0:
        break
    command = input()
difference = abs(all_pieces)
if all_pieces > 0:
    print(f"{all_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {difference} pieces more.")