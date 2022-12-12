command = input()
sum_steps = 0
steps_end_day = 0

while command != "Going home":
    steps_for_day = int(command)
    sum_steps += steps_for_day
    if sum_steps >= 10000:
        break
    command = input()
if command == "Going home":
    steps_end_day = int(input())

sum_all_steps = sum_steps + steps_end_day
difference = abs(sum_all_steps - 10000)
if sum_all_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")