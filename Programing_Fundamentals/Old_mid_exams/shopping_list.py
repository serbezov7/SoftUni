def urgent(shopping_list_, item_):
    if item_ not in shopping_list_:
        shopping_list_.insert(0, item_)
    return shopping_list_


def unnecessary(shopping_list_, item_):
    if item_ in shopping_list_:
        shopping_list_.remove(item_)
    return shopping_list_


def correct(shopping_list_, old_item_, new_item_):
    if old_item_ in shopping_list_:
        index = shopping_list_.index(old_item_)
        shopping_list_[index] = new_item_
    return shopping_list_


def rearrange(shopping_list_, item_):
    if item_ in shopping_list_:
        index = shopping_list_.index(item_)
        shopping_list_.append(shopping_list_.pop(index))
    return shopping_list_


shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    current_command = command[0]
    if current_command == "Urgent":
        item = command[1]
        shopping_list = urgent(shopping_list, item)
    elif current_command == "Unnecessary":
        item = command[1]
        shopping_list = unnecessary(shopping_list, item)
    elif current_command == "Correct":
        old_item = command[1]
        new_item = command[2]
        shopping_list = correct(shopping_list, old_item, new_item)
    elif current_command == "Rearrange":
        item = command[1]
        shopping_list = rearrange(shopping_list, item)

    command = input()
print(", ".join(shopping_list))
