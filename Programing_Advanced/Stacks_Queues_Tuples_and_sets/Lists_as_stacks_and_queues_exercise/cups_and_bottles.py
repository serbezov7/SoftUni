from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]
wasted_water = 0

while cups_capacity and bottles_capacity:
    current_bottle = bottles_capacity.pop()
    current_cup = cups_capacity.popleft()

    while current_cup:
        difference = current_bottle - current_cup
        if difference >= 0:
            wasted_water += difference
            break
        else:
            current_cup = abs(difference)
            current_bottle = bottles_capacity.pop()

if bottles_capacity:
    print(f"Bottles: {' '.join(str(x) for x in reversed(bottles_capacity))}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
    print(f"Wasted litters of water: {wasted_water}")