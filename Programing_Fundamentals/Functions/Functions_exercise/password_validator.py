def long_check(password):
    if len(password) > 10 or len(password) < 6:
        return False
    else:
        return True


def letters_and_digit(password):
    return password.isalnum()


def two_digit(password):
    counter = 0
    for current_num in password:
        if current_num.isdigit():
            counter += 1
    if counter < 2:
        return False
    else:
        return True


current_password = input()
if not long_check(current_password):
    print("Password must be between 6 and 10 characters")
if not letters_and_digit(current_password):
    print("Password must consist only of letters and digits")
if not two_digit(current_password):
    print("Password must have at least 2 digits")
if long_check(current_password) and two_digit(current_password) and letters_and_digit(current_password):
    print("Password is valid")
