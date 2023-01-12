command = input()
initial_dict = {}

while command != "end of contests":
    current_command = command.split(":")
    contest = current_command[0]
    password = current_command[1]
    initial_dict[contest] = password
    command = input()

second_command = input()
result_dict = {}
while second_command != "end of submissions":
    new_command = second_command.split("=>")
    check_contest = new_command[0]
    check_password = new_command[1]
    username = new_command[2]
    points = int(new_command[3])
    if check_contest in initial_dict.keys():
        if check_password == initial_dict[check_contest]:
            if username not in result_dict.keys():
                result_dict[username] = {check_contest: points}
            else:
                for key in result_dict[username].keys():
                    if check_contest in result_dict[username].keys():
                        if result_dict[username][check_contest] < points:
                            result_dict[username][check_contest] = points
                        break
                else:
                    result_dict[username][check_contest] = points

    second_command = input()
candidate = ""
best_points = 0
for key_name in result_dict.keys():
    total_points = 0
    for current_points in result_dict[key_name].values():
        total_points += current_points
    if total_points > best_points:
        best_points = total_points
        candidate = key_name
print(f"Best candidate is {candidate} with total {best_points} points.\nRanking:")
sorted_names = sorted(result_dict.keys(), key=lambda x: x[0])

for user in sorted_names:
    print(user)
    for contest, points in sorted(result_dict[user].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")

