def age_assignment(*args, **kwargs):
    result = []
    for name in sorted(args):
        for letter, age in kwargs.items():
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return "\n".join(result)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))