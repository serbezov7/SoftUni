fire_list = input().split("#")
water_left = int(input())
total_fire = 0
fire_putted_out = []

for current_fire in fire_list:
    current_fire = current_fire.split(" = ")
    fire_value = int(current_fire[1])
    if current_fire[0] == "High":
        if 81 <= fire_value <= 125:
            if water_left >= fire_value:
                water_left -= fire_value
                total_fire += fire_value
                fire_putted_out.append(fire_value)
    elif current_fire[0] == "Medium":
        if 51 <= fire_value <= 80:
            if water_left >= fire_value:
                water_left -= fire_value
                total_fire += fire_value
                fire_putted_out.append(fire_value)
    elif current_fire[0] == "Low":
        if 1 <= fire_value <= 50:
            if water_left >= fire_value:
                water_left -= fire_value
                total_fire += fire_value
                fire_putted_out.append(fire_value)

effort = total_fire * 0.25
print("Cells:")
for fire in fire_putted_out:
    print(f" - {fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
