change = float(input())
transform_change = round(change * 100)
coins_count = 0
while transform_change > 0:
    if transform_change >= 200:
        transform_change -= 200
    elif transform_change >= 100:
        transform_change -= 100
    elif transform_change >= 50:
        transform_change -= 50
    elif transform_change >= 20:
        transform_change -= 20
    elif transform_change >= 10:
        transform_change -= 10
    elif transform_change >= 5:
        transform_change -= 5
    elif transform_change >= 2:
        transform_change -= 2
    elif transform_change >= 1:
        transform_change -= 1
    coins_count += 1
print(coins_count)