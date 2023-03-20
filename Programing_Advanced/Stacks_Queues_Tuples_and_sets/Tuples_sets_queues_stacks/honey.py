from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

operations = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue
    if current_nectar == 0:
        continue

    current_symbol = symbols.popleft()
    result = abs(operations[current_symbol](int(current_bee), int(current_nectar)))
    total_honey += result

print(f"Total honey made: {total_honey}")
print(f"Bees left: {', '.join(str(x) for x in bees)}") if bees else None
print(f"Nectar left: {', '.join(str(x) for x in nectar)}") if nectar else None
