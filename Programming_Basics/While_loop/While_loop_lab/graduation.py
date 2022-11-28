name = input()
grade = 1
sum_evaluation = 0
excluded = 0
is_excluded = False

while grade <= 12:
    evaluation = float(input())
    if evaluation < 4:
        excluded += 1
        if excluded > 1:
            is_excluded = True
            break
        continue
    else:
        grade += 1
        sum_evaluation += evaluation
if is_excluded:
    print(f"{name} has been excluded at {grade} grade")
else:
    average_evaluation = sum_evaluation / 12
    print(f"{name} graduated. Average grade: {average_evaluation:.2f}")
