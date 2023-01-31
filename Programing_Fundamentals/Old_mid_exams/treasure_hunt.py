def loot(init_loot_, command_):
    last_loot_items_ = []
    for index_, item_ in enumerate(command_):
        if index_ == 0:
            continue
        if item_ not in init_loot_:
            init_loot_.insert(0, item_)
            last_loot_items_.append(item_)
    return last_loot_items_, init_loot_


def drop(init_loot_, index_):
    if index in range(len(init_loot_)):
        init_loot_.append(init_loot_.pop(index_))
    return init_loot_


def steal(init_loot_, count_):
    init_loot_copy = init_loot_.copy()
    removed_list = []
    if count_ not in range(len(init_loot_)):
        count_ = len(init_loot_)
    for index_ in range(len(init_loot_) - count_, len(init_loot_)):
        removed_list.append(init_loot_[index_])
        init_loot_copy.remove(init_loot_[index_])
    init_loot_ = init_loot_copy
    print(", ".join(removed_list))
    return init_loot_


init_loot = input().split("|")
command = input().split()

while command[0] != "Yohoho!":
    current_command = command[0]
    if current_command == "Loot":
        last_loot_items, init_loot = loot(init_loot, command)
    elif current_command == "Drop":
        index = int(command[1])
        init_loot = drop(init_loot, index)
    elif current_command == "Steal":
        count = int(command[1])
        init_loot = steal(init_loot, count)

    command = input().split()

if len(init_loot) > 0:
    total_length = 0
    for item in init_loot:
        total_length += len(item)
    average_gain = total_length / len(init_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
