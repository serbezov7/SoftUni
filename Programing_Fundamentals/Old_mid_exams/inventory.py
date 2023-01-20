def collect(initial_items_, item_):
    if item_ not in initial_items_:
        initial_items_.append(item_)
    return initial_items_


def drop(initial_items_, item_):
    if item_ in initial_items_:
        initial_items_.remove(item_)
    return initial_items_


def combine(initial_items_, old_item_, new_item_):
    if old_item_ in initial_items_:
        old_index = initial_items_.index(old_item_)
        initial_items_.insert(old_index + 1, new_item_)
    return initial_items_


def renew(initial_items_, item_):
    if item_ in initial_items_:
        index = initial_items_.index(item_)
        initial_items_.append(initial_items_.pop(index))
    return initial_items_


initial_items = input().split(", ")
command = input().split(" - ")

while command[0] != "Craft!":
    current_command, item = command
    if current_command == "Collect":
        initial_items = collect(initial_items, item)
    elif current_command == "Drop":
        initial_items = drop(initial_items, item)
    elif current_command == "Combine Items":
        old_item, new_item = item.split(":")
        initial_items = combine(initial_items, old_item, new_item)
    elif current_command == "Renew":
        initial_items = renew(initial_items, item)

    command = input().split(" - ")

print(", ".join(initial_items))
