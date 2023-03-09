number_of_students = int(input())
students_dict = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students_dict.keys():
        students_dict[name] = []
    students_dict[name].append(float(grade))

for student, grades in students_dict.items():
    grades_to_str = " ".join(map(lambda x: f"{x:.2f}", grades))
    average = sum(grades) / len(grades)
    print(f"{student} -> {grades_to_str} (avg: {average:.2f})")

