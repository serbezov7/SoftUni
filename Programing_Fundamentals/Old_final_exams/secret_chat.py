def insert_space(message_, index_):
    message_ = message_[:index_] + " " + message[index_:]
    print(message_)
    return message_


def reverse(message_, substring_):
    if substring_ in message_:
        message_ = message_.replace(substring_, "", 1) + substring_[::-1]
        print(message_)

    else:
        print("error")
    return message_


def change(message_, substring_, replacement_):
    if substring_ in message_:
        message_ = message_.replace(substring_, replacement_)
        print(message_)
    return message_


message = input()
command = input().split(":|:")

while command[0] != "Reveal":
    if command[0] == "InsertSpace":
        index = int(command[1])
        message = insert_space(message, index)
    elif command[0] == "Reverse":
        substring = command[1]
        message = reverse(message, substring)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = change(message, substring, replacement)

    command = input().split(":|:")

print(f"You have a new text message: {message}")
