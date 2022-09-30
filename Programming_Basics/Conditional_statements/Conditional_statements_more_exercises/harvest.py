import math
from math import ceil , floor
total_vine = int(input())
vine_kg_per_square = float(input())
needed_vine = int(input())
workers = int(input())
total_vine_ltr = (total_vine * 0.4) * vine_kg_per_square / 2.5
difference = abs(total_vine_ltr - needed_vine)
diff_per_worker = difference / workers

if total_vine_ltr < needed_vine:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(total_vine_ltr)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(diff_per_worker)} liters per person.")


