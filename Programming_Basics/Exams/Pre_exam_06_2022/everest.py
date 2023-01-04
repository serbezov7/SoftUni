command = input()
days = 1
starting_point = 5364
total_climbed = 0
is_climbed = False

while command != "END":
    if command == "Yes":
        days += 1
        if days > 5:
            break
    climbed_meters = int(input())
    total_climbed = starting_point + climbed_meters
    starting_point = total_climbed
    if total_climbed >= 8848:
        is_climbed = True
        break

    command = input()
if is_climbed:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(total_climbed)
