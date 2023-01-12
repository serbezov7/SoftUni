command = input()
course_dict = {}

while command != "end":
    course_name, students_name = command.split(" : ")
    if course_name not in course_dict.keys():
        course_dict[course_name] = [students_name]
    else:
        course_dict[course_name] += [students_name]

    command = input()
for name in course_dict.keys():
    print(f"{name}: {len(course_dict[name])}")
    for attended in course_dict[name]:
        print(f"-- {attended}")
