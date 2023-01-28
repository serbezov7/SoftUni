first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
waiting_students = int(input())
students_per_hour = first_employee + second_employee + third_employee
hour = 0
while waiting_students > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    waiting_students -= students_per_hour
print(f"Time needed: {hour}h.")
