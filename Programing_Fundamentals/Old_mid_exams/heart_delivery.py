houses = list(map(int, input().split("@")))
command = input().split()
current_index = 0

while command[0] != "Love!":
    jump_index = int(command[1]) + current_index
    if jump_index > len(houses) - 1:
        jump_index = 0
    if houses[jump_index] == 0:
        print(f"Place {jump_index} already had Valentine's day.")
    else:
        houses[jump_index] -= 2
        if houses[jump_index] == 0:
            print(f"Place {jump_index} has Valentine's day.")
    current_index = jump_index

    command = input().split()

failed_count = 0
for house in houses:
    if house != 0:
        failed_count += 1
print(f"Cupid's last position was {current_index}.")
if failed_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_count} places.")
