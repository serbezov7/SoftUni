initial_energy = int(input())
command = input()
count = 0
while command != "End of battle":
    distance = int(command)
    if initial_energy >= distance:
        initial_energy -= distance
        count += 1
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {initial_energy} energy")
        break
    if count % 3 == 0:
        initial_energy += count

    command = input()
if command == "End of battle":
    print(f"Won battles: {count}. Energy left: {initial_energy}")
