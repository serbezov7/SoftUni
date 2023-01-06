loss_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_expences = loss_fights // 2 * helmet_price
sword_expences = loss_fights // 3 * sword_price
shield_expences = loss_fights // 6 * shield_price
armor_expences = loss_fights // 12 * armor_price
total_expences = helmet_expences + sword_expences + shield_expences + armor_expences

print(f"Gladiator expenses: {total_expences:.2f} aureus")

