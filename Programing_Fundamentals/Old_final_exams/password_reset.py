def takeodd(password_):
    new_password = ""
    for index in range(len(password_)):
        if index % 2 != 0:
            new_password += password_[index]
    print(new_password)
    return new_password


def cut(password_, index_, length_):
    substring = password_[index_:index + length_]
    password_ = password_.replace(substring, "", 1)
    print(password_)
    return password_


def replace(password_, substring_, substitute_):
    if substring_ in password_:
        password_ = password_.replace(substring_, substitute_)
        print(password_)
    else:
        print("Nothing to replace!")
    return password_


password = input()
command = input().split()

while command[0] != "Done":
    if command[0] == "TakeOdd":
        password = takeodd(password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = cut(password, index, length)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        password = replace(password, substring, substitute)

    command = input().split()

print(f"Your password is: {password}")
