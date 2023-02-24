from collections import deque

data = deque([[int(x) for x in input().split()]for _ in range(int(input()))])
data_copy = data.copy()
tank = 0
index = 0
while data_copy:
    liters, distance = data_copy.popleft()
    tank += liters
    if tank < distance:
        data.rotate(-1)
        data_copy = data.copy()
        index += 1
        tank = 0
    else:
        tank -= distance
print(index)
