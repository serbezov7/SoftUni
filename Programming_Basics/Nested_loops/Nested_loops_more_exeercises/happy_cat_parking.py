total_days = int(input())
hours_per_day = int(input())
total_price = 0

for day in range(1, total_days + 1):
    total_day_price = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
            total_day_price += price
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
            total_day_price += price
        else:
            price = 1
            total_day_price += price
    total_price += total_day_price
    print(f"Day: {day} - {total_day_price:.2f} leva")
print(f"Total: {total_price:.2f} leva")