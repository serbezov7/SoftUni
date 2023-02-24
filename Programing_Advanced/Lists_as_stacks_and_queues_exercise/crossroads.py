from collections import deque

green = int(input())
init_green = green
free_window = int(input())
cars_queue = deque()
counter = 0
flag = False
command = input()
while command != "END":
    if command != "green":
        cars_queue.append(command)

    else:
        green = init_green
        while cars_queue and green > 0:
            current_car = cars_queue.popleft()
            if len(current_car) - green - free_window > 0:
                print(f"A crash happened!\n{current_car} was hit at {current_car[green + free_window]}.")
                flag = True
                break
            else:
                counter += 1
                green -= len(current_car)
        if flag:
            break

    command = input()
else:
    print(f"Everyone is safe.\n{counter} total cars passed the crossroads.")

