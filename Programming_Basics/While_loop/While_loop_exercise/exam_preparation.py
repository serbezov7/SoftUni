bad_tries = int(input())
bad_tries_count = 0
all_grades = 0
number_of_problems = 0
last_problem = ""
is_excluded = False
command = input()
while command != "Enough":
    grade = int(input())
    all_grades += grade
    number_of_problems += 1
    last_problem = command
    if grade <= 4:
        bad_tries_count += 1
        if bad_tries_count >= bad_tries:
            is_excluded = True
            break
    command = input()
average_score = all_grades / number_of_problems
if is_excluded:
    print(f"You need a break, {bad_tries_count} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")