quantity_of_decorations = int(input())
days_until_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 23
if days_until_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
