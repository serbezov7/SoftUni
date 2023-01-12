def length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def contain_validation(name):
    for letter in name:
        if not (letter.isalnum() or letter == "-" or letter == "_"):
            return False
    return True
    # is_valid = True
    # for letter in name:
    #     if letter.isalnum() or letter == "-" or letter == "_":
    #         continue
    #     is_valid = False
    # if is_valid:
    #     return True
    # return False


def redundant_check(name):
    if " " not in name:
        return True
    return False


def call_func(name):
    if length(name) and contain_validation(name) and redundant_check(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if call_func(username):
        print(username)
