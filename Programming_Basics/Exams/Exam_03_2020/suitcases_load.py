capacity = float(input())
counter = 0
luggage = 0
command = input()
while command != "End":
    volume_luggage = float(command)
    counter += 1
    if counter % 3 == 0:
        volume_luggage *= 1.10
    if capacity < volume_luggage:
        print("No more space!")
        break
    capacity -= volume_luggage
    luggage += 1
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {luggage} suitcases loaded.")

# trunk_capacity = float(input())
# current_volume = 0
# count_luggages = 0
# counter = 0
# difference = 0
# is_trunk_full = False
# command = input()
# while command != "End":
#     suitcase_volume = float(command)
#     counter += 1
#     current_volume += suitcase_volume
#     if counter % 3 == 0:
#         difference = suitcase_volume
#         suitcase_volume = round(suitcase_volume * 1.10 - difference)
#         current_volume += suitcase_volume
#     if current_volume >= trunk_capacity:
#         is_trunk_full = True
#         break
#     count_luggages += 1
#     command = input()
# if is_trunk_full:
#     print("No more space!")
# else:
#     print("Congratulations! All suitcases are loaded!")
# print(f"Statistic: {count_luggages} suitcases loaded.")