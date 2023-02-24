clothes = list(map(int, (input().split())))

init_capacity = int(input())
capacity = init_capacity
racks = 1

while clothes:
    cloth = clothes.pop()
    if capacity - cloth >= 0:
        capacity -= cloth
    else:
        racks += 1
        capacity = init_capacity
        capacity -= cloth

print(racks)
