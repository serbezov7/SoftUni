command = input().split(":")
my_dict = {}

while len(command) > 1:
    name, student_id, course = command[0], command[1], command[2]
    if course not in my_dict:
        my_dict[course] = []
    my_dict[course] += [f"{name} - {student_id}"]
    command = input().split(":")

command = command[0].replace("_", " ")
print("\n".join(my_dict[command]))
# for course in my_dict[command]:
#     print(course)
