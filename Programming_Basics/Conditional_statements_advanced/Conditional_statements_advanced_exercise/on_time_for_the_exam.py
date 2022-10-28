exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_minutes_exam = exam_hour * 60 + exam_minutes
total_minutes_arrival = arrival_hour * 60 + arrival_minutes
difference = abs(total_minutes_exam - total_minutes_arrival)

if total_minutes_arrival > total_minutes_exam:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
elif total_minutes_arrival == total_minutes_exam or difference <= 30:
    print("On Time")
    if 1 <= difference <= 30:
        print(f"{difference} minutes before the start")
else:
    print("Early")
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
