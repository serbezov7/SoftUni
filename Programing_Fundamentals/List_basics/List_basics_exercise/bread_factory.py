events = input().split("|")
energy = 100
coins = 100
all_events_managed = True

for event in events:
    command, value = event.split("-")
    value = int(value)
    if command == "rest":
        initial_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            all_events_managed = False
            break
if all_events_managed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
