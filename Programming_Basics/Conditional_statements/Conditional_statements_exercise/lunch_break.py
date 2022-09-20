import math

series = input()
duration_ep = int(input())
duration_break = int(input())

lunch_break = duration_break * 0.125
relax_time = duration_break * 0.25
time_left = duration_break - lunch_break - relax_time

difference = abs(time_left - duration_ep)
difference = math.ceil(difference)
if time_left >= duration_ep:
    print(f"You have enough time to watch {series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {difference} more minutes.")
