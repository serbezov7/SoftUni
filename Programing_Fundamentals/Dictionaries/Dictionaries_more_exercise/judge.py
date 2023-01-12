command = input()
courses_dict = {}
users_dict = {}

while command != "no more time":
    current_command = command.split(" -> ")
    username = current_command[0]
    contest = current_command[1]
    points = int(current_command[2])
    if contest not in courses_dict.keys():
        courses_dict[contest] = {username: points}
    else:
        for name in courses_dict[contest].keys():
            if name == username:
                if courses_dict[contest][username] < points:
                    courses_dict[contest][username] = points
                break
        else:
            courses_dict[contest][username] = points

    command = input()

for course in courses_dict.keys():
    total_points = 0
    for name, points in courses_dict[course].items():
        if name not in users_dict.keys():
            users_dict[name] = points
        else:
            users_dict[name] += points

for course in courses_dict.keys():
    count = 1
    print(f"{course}: {len(courses_dict[course])} participants")
    for name, points in sorted(courses_dict[course].items(), key=lambda x: (-x[1], x[0])):
        print(f"{count}. {name} <::> {points}")
        count += 1
print("Individual standings:")
counter = 1
for name, points in sorted(users_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {name} -> {points}")
    counter += 1
