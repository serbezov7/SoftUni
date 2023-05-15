from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidUsernameError(Exception):
    pass


email = input()
while email != "End":
    domains = [".com", ".bg", ".org", ".net"]
    domain_pattern = r"\.[a-z]+"
    username_pattern = r"[\w\.]+"
    try:
        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if findall(domain_pattern, email)[-1] not in domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        if findall(username_pattern, email)[0] != email.split("@")[0]:
            raise InvalidUsernameError("Username can only contain letters, numbers, dots and underscores")

        print("Email is valid")

    except IndexError:
        print("Invalid email")

    email = input()
