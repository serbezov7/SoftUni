rest_days = int(input())
work_days = 365 - rest_days
play_work = work_days * 63
play_rest_days = rest_days * 127
total_play_time = play_work + play_rest_days
difference = abs(30000 - total_play_time)
difference_hours = difference // 60
difference_minutes = difference % 60

if total_play_time > 30000:
    print("Tom will run away")
    print(f"{difference_hours} hours and {difference_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{difference_hours} hours and {difference_minutes} minutes less for play")
