from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
crafted_presents = {}
toys = {"Doll", "Wooden train", "Teddy bear", "Bicycle"}

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()

    if current_material == 0 and current_magic == 0:
        continue
    if current_material == 0:
        magic_level.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials.append(current_material)
        continue

    result = current_material * current_magic
    if result < 0:
        materials.append(current_material + current_magic)
    elif result not in presents.keys():
        materials.append(current_material + 15)
    else:
        toy = presents[result]
        if toy not in crafted_presents.keys():
            crafted_presents[toy] = 0
        crafted_presents[toy] += 1

if "Bicycle" in crafted_presents.keys() and "Teddy bear" in crafted_presents.keys() or\
        "Doll" in crafted_presents.keys() and "Wooden train" in crafted_presents.keys():
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}") if materials else None
print(f"Magic left: {', '.join(str(x) for x in magic_level)}") if magic_level else None
for name, amount in sorted(crafted_presents.items()):
    print(f"{name}: {amount}")
