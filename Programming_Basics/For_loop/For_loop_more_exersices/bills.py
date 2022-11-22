months = int(input())
water = 20
internet = 15
sum_water = water * months
sum_internet = internet * months
sum_electricity = 0
sum_other = 0
for month in range(months):
    electricity = float(input())
    sum_other += (water + internet + electricity) * 1.2
    sum_electricity += electricity
sum_all = (sum_water + sum_internet + sum_electricity + sum_other) / months
print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {sum_other:.2f} lv")
print(f"Average: {sum_all:.2f} lv")