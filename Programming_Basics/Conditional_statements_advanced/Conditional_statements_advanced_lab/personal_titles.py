age = float(input())
gender = input()

if gender == "m":
    if 0 < age < 16:
        print("Master")
    else:
        print("Mr.")
elif gender == "f":
    if 0 < age < 16:
        print("Miss")
    else:
        print("Ms.")


