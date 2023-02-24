from _collections import deque

my_queue = deque()
while True:
    name = input()
    if name == "Paid":
        for _ in range(len(my_queue)):
            print(my_queue.popleft())
    elif name == "End":
        print(f"{len(my_queue)} people remaining.")
        break

    else:
        my_queue.append(name)
