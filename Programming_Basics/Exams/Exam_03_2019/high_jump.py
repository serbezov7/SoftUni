goal = int(input())
current_high = goal - 30
all_jumps = 0
miss_try = 0
is_failed = False
while current_high <= goal:

    jump = int(input())
    while current_high >= jump:
        miss_try += 1
        all_jumps += 1
        if miss_try == 3:
            is_failed = True
            break
        jump = int(input())
    if is_failed:
        break
    if jump > current_high:
        miss_try = 0
        current_high += 5
        all_jumps += 1
if is_failed:
    print(f"Tihomir failed at {current_high}cm after {all_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {goal}cm after {all_jumps} jumps.")