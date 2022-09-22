time_first = int(input())
time_second = int(input())
time_third = int(input())

minutes = (time_first + time_second + time_third) // 60
seconds = (time_first + time_second + time_third) % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
