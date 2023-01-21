def fire(warship_, index_, damage_):
    flag_ = False
    if index_ in range(len(warship_)):
        warship_[index_] -= damage_
        if warship_[index_] <= 0:
            print("You won! The enemy ship has sunken.")
            flag_ = True

    return flag_, warship_


def defend(pirate_ship_, start_index_, end_index_, damage_):
    flag_ = False
    if start_index_ in range(len(pirate_ship_)) and end_index_ in range(len(pirate_ship_)):
        for section in range(start_index_, end_index_ + 1):
            pirate_ship_[section] -= damage_
            if pirate_ship_[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                flag_ = True
                break

    return flag_, pirate_ship_


def repair(pirate_ship_, index_, health_):
    if index_ in range(len(pirate_ship_)):
        pirate_ship_[index_] += health_
        if pirate_ship_[index_] > health_capacity:
            pirate_ship_[index_] = health_capacity
    return pirate_ship_


def status(pirate_ship_):
    count_section = len([x for x in pirate_ship_ if x < health_capacity * 0.20])

    print(f"{count_section} sections need repair.")


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
health_capacity = int(input())
command = input().split()
flag = False
while command[0] != "Retire":
    current_command = command[0]
    if current_command == "Fire":
        index = int(command[1])
        damage = int(command[2])
        flag, warship = fire(warship, index, damage)
        if flag:
            break
    elif current_command == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        flag, pirate_ship = defend(pirate_ship, start_index, end_index, damage)
        if flag:
            break
    elif current_command == "Repair":
        index = int(command[1])
        health = int(command[2])
        pirate_ship = repair(pirate_ship, index, health)
    elif current_command == "Status":
        status(pirate_ship)

    command = input().split()

if not flag:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
