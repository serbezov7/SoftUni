def add(lesson, courses):
    if lesson not in courses:
        courses.append(lesson)


def insert(lesson, index_, courses):
    if lesson not in courses:
        courses.insert(index_, lesson)


def remove(lesson, courses):
    if lesson in courses:
        courses.remove(lesson)
        if f"{lesson}-Exercise" in courses:
            courses.remove(f"{lesson}-Exercise")


def swap(first_lesson, second_lesson, courses):
    if first_lesson in courses and second_lesson in courses:
        first_index = courses.index(first_lesson)
        second_index = courses.index(second_lesson)
        courses[first_index], courses[second_index] = courses[second_index], courses[first_index]
        if first_index + 1 <= len(courses) - 1 and second_index + 1 <= len(courses) - 1:
            if "Exercise" in courses[first_index + 1]:
                courses.insert(second_index + 1, courses.pop(first_index + 1))
            if "Exercise" in courses[second_index + 1]:
                courses.insert(first_index + 1, courses.pop(second_index + 1))


def exercise(lesson, courses):
    if lesson in courses and f"{lesson}-Exercise" not in courses:
        lesson_index = courses.index(lesson)
        courses.insert(lesson_index + 1, f"{lesson}-Exercise")
    elif lesson not in courses and f"{lesson}-Exercise" not in courses:
        courses.append(lesson)
        courses.append(f"{lesson}-Exercise")


initial_courses = input().split(", ")
command = input().split(":")

while command[0] != "course start":
    current_command = command[0]
    lesson_title = command[1]
    if current_command == "Add":
        add(lesson_title, initial_courses)
    elif current_command == "Insert":
        index = int(command[2])
        insert(lesson_title, index, initial_courses)
    elif current_command == "Remove":
        remove(lesson_title, initial_courses)
    elif current_command == "Swap":
        second_course = command[2]
        swap(lesson_title, second_course, initial_courses)
    elif current_command == "Exercise":
        exercise(lesson_title, initial_courses)
    command = input().split(":")

for index, course in enumerate(initial_courses):
    print(f"{index + 1}.{course}")
