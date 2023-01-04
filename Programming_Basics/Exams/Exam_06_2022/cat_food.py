count_of_cats = int(input())
group_one = 0
group_two = 0
group_three = 0
total_eaten_food = 0

for food in range(count_of_cats):
    eaten_food = float(input())
    if eaten_food < 200:
        group_one += 1
        total_eaten_food += eaten_food
    elif eaten_food < 300:
        group_two += 1
        total_eaten_food += eaten_food
    else:
        group_three += 1
        total_eaten_food += eaten_food
price_food = total_eaten_food / 1000 * 12.45

print(f"Group 1: {group_one} cats.")
print(f"Group 2: {group_two} cats.")
print(f"Group 3: {group_three} cats.")
print(f"Price for food per day: {price_food:.2f} lv.")