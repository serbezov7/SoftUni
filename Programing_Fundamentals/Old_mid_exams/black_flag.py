days = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
collected_plunder = 0

for day in range(1, days + 1):
    collected_plunder += plunder_per_day
    if day % 3 == 0:
        collected_plunder += plunder_per_day * 0.50
    if day % 5 == 0:
        collected_plunder *= 0.70

if collected_plunder >= expected_plunder:
    print(f"Ahoy! {collected_plunder:.2f} plunder gained.")
else:
    percentage = collected_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
