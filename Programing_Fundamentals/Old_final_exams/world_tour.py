def add(stops_, index_, new_stop_):
    if index_ in range(len(stops_)):
        left = stops_[0:index]
        right = stops_[index_:len(stops_)]
        stops_ = left + new_stop_ + right
    return stops_


def remove(stops_, start_index_, end_index_):
    if start_index_ in range(len(stops_)) and end_index_ in range(len(stops_)):
        left = stops_[0:start_index_]
        right = stops_[end_index_ + 1: len(stops_)]
        stops_ = left + right
    return stops_


def switch(stops_, old_string_, new_string_):
    return stops_.replace(old_string_, new_string_)


stops = input()
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        new_stop = command[2]
        stops = add(stops, index, new_stop)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        stops = remove(stops, start_index, end_index)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)

    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")
