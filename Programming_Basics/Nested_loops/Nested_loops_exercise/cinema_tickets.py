command = input()
all_tickets = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0

while command != "Finish":
    name_of_the_movie = command
    all_seats = int(input())
    tickets_count = 0
    type_of_the_ticket = input()
    while type_of_the_ticket != "End":
        tickets_count += 1
        all_tickets += 1
        if type_of_the_ticket == "student":
            student_ticket += 1
        elif type_of_the_ticket == "standard":
            standard_ticket += 1
        else:
            kids_ticket += 1

        if tickets_count == all_seats:
            break
        type_of_the_ticket = input()
    percent_full = tickets_count / all_seats * 100
    print(f"{name_of_the_movie} - {percent_full:.2f}% full.")

    command = input()
percent_students_ticket = student_ticket / all_tickets * 100
percent_standard_ticket = standard_ticket / all_tickets * 100
percent_kids_ticket = kids_ticket / all_tickets * 100

print(f"Total tickets: {all_tickets}")
print(f"{percent_students_ticket:.2f}% student tickets.")
print(f"{percent_standard_ticket:.2f}% standard tickets.")
print(f"{percent_kids_ticket:.2f}% kids tickets.")
