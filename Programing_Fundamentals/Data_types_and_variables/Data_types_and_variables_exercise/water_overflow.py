lines = int(input())
capacity = 255
liters_poured = 0

for liters in range(lines):
    current_liters = int(input())
    if capacity - current_liters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= current_liters
    liters_poured += current_liters
print(liters_poured)
