from collections import deque


def add_names():
    my_queue_ = deque()
    name = input()
    while name != "Start":
        my_queue_.append(name)
        name = input()
    return my_queue_


capacity = int(input())
my_queue = add_names()
command = input().split()

while command[0] != "End":
    if command[0] == "refill":
        quantity = int(command[1])
        capacity += quantity
    else:
        needed_liters = int(command[0])
        person = my_queue.popleft()
        if capacity >= needed_liters:
            capacity -= needed_liters
            print(f"{person} got water" )
        else:
            print(f"{person} must wait")

    command = input().split()
print(f"{capacity} liters left")
