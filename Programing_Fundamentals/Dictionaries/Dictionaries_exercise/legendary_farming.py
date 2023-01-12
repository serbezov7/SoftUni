materials = input().split()
materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
while True:
    obtained = False
    for current_material in range(0, len(materials), 2):
        quantity = int(materials[current_material])
        material = materials[current_material + 1].lower()

        if material not in materials_dict.keys():
            materials_dict[material] = 0
        materials_dict[material] += quantity

        if materials_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials_dict[material] -= 250
            obtained = True
        elif materials_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            materials_dict[material] -= 250
            obtained = True
        elif materials_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials_dict[material] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    materials = input().split()

for rest_material, rest_quantity in materials_dict.items():
    print(f"{rest_material}: {rest_quantity}")



