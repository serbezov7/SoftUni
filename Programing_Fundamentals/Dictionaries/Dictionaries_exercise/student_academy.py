pair_of_rows = int(input())
students_dict = {}
average_dict = {}
for pair in range(pair_of_rows):
    student = input()
    grade = float(input())
    if student not in students_dict.keys():
        students_dict[student] = []
    students_dict[student].append(grade)
for current_student, current_grade in students_dict.items():
    average = sum(current_grade) / len(current_grade)
    if average >= 4.50:
        average_dict[current_student] = average
        print(f"{current_student} -> {average:.2f}")
