people = int(input())
total_grade = 0
presentation_count = 0
command = input()
while command != "Finish":
    presentation = command
    presentation_count += 1
    sum_grade = 0
    for i in range(people):
        grade = float(input())
        sum_grade += grade
    avg_sum = sum_grade / people
    total_grade += avg_sum
    print(f"{presentation} - {avg_sum:.2f}.")
    command = input()
total_avg = total_grade / presentation_count
print(f"Student's final assessment is {total_avg:.2f}.")
