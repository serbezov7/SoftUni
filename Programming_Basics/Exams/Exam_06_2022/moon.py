from math import ceil
average_speed = float(input())
liters_per_100_km = float(input())
total_distance = 2 * 384400
time = ceil(total_distance / average_speed) + 3
liters_fuel = liters_per_100_km * total_distance / 100
print(time)
print(int(liters_fuel))
