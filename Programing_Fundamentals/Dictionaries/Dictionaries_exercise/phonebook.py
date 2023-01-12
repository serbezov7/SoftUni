command = input()
phone_dict = {}

while "-" in command:
    name, number = command.split("-")
    phone_dict[name] = number

    command = input()

count_people = int(command)

for contact in range(count_people):
    searched_contact = input()
    if searched_contact in phone_dict.keys():
        print(f"{searched_contact} -> {phone_dict[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
