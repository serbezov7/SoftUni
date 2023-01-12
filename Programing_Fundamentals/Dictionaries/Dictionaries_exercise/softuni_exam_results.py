command = input()
students_dict = {}
courses_dict = {}
while command != "exam finished":
    current_command = command.split("-")
    if "banned" in current_command:
        name = current_command[0]
        del students_dict[name]
    else:
        username = current_command[0]
        language = current_command[1]
        points = int(current_command[2])
        if username not in students_dict.keys():
            students_dict[username] = 0
        if students_dict[username] < points:
            students_dict[username] = points
        if language not in courses_dict:
            courses_dict[language] = 0
        courses_dict[language] += 1

    command = input()
print("Results:")
for key, value in students_dict.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in courses_dict.items():
    print(f"{key} - {value}")
