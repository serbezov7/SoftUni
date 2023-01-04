minutes = int(input())
seconds = int(input())
length = float(input())
seconds_for_hundred_meters = int(input())
needed_time = minutes * 60 + seconds
bonus_time = length / 120 * 2.50
competitor_time = length / 100 * seconds_for_hundred_meters - bonus_time
if competitor_time <= needed_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitor_time:.3f}.")
else:
    difference = competitor_time - needed_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")