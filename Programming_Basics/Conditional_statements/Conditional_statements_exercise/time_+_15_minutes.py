hour_first = int(input())
minutes_first = int(input())

total = (hour_first * 60) + minutes_first + 15

hour = total // 60
minutes = total % 60
if hour > 23:
    hour = 0
if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")

