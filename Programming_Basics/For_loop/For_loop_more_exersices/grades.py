students = int(input())
top_students = 0
between_4_5 = 0
between_3_4 = 0
under_3 = 0
all_evaluation = 0

for student in range(students):
    evaluation = float(input())
    all_evaluation += evaluation
    if evaluation < 3:
        under_3 += 1
    elif evaluation < 4:
        between_3_4 += 1
    elif evaluation < 5:
        between_4_5 += 1
    else:
        top_students +=1
percent_top = top_students / students * 100
percent_4_5 = between_4_5 / students * 100
percent_3_4 = between_3_4 / students * 100
percent_fail = under_3 / students * 100
average = all_evaluation / students
print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_3_4:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average:.2f}")