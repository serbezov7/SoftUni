from math import floor
current_record = float(input())
distance = float(input())
time_for_one_meter = float(input())
time = distance * time_for_one_meter
delay = floor(distance / 50) * 30
total_time = time + delay
difference = abs(current_record - total_time)
if total_time < current_record:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")