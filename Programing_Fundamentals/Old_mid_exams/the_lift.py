people_waiting = int(input())
current_state = list(map(int, input().split()))
flag = False
for index, current_wagon in enumerate(current_state):
    difference = 4 - current_wagon
    if difference <= people_waiting:
        current_state[index] += difference
        people_waiting -= difference
    else:
        current_state[index] += people_waiting
        people_waiting -= people_waiting
        flag = True
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

elif flag:
    print("The lift has empty spots!")

print(' '.join(str(x) for x in current_state))