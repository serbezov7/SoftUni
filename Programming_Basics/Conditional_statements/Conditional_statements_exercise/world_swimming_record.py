record = float(input())
distance = float(input())
time_for_meter = float(input())

sum_time = time_for_meter * distance
delay = distance // 15 * 12.5
time_with_delay = sum_time + delay
difference = abs(record - time_with_delay)
if time_with_delay < record:
    print(f"Yes, he succeeded! The new world record is {time_with_delay:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
