def shoot(targets_, index_, power_):
    if index_ in range(len(targets_)):
        if targets_[index_] - power_ > 0:
            targets_[index_] -= power_
        else:
            targets_.pop(index_)
    return targets_


def add(targets_, index_, value_):
    if index_ in range(len(targets_)):
        targets_.insert(index_, value_)
    else:
        print("Invalid placement!")
    return targets_


def strike(targets_, index_, radius_):
    starting_index = index_ - radius_
    finish_index = index_ + radius_
    if starting_index in range(len(targets_)) and finish_index in range(len(targets_)):
        targets_ = [targets_[x] for x in range(len(targets_)) if x\
                    not in range(starting_index, finish_index + 1)]
    else:
        print("Strike missed!")
    return targets_


targets = list(map(int, input().split()))
command = input().split()

while command[0] != "End":
    current_command = command[0]
    index = int(command[1])
    if current_command == "Shoot":
        power = int(command[2])
        targets = shoot(targets, index, power)
    elif current_command == "Add":
        value = int(command[2])
        targets = add(targets, index, value)
    elif current_command == "Strike":
        radius = int(command[2])
        targets = strike(targets, index, radius)

    command = input().split()
print("|".join(str(x) for x in targets))

