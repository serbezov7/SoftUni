control_number = int(input())
counter = 0
password = ""
is_combination_found = False
is_password_find = False

for a in range(1, 10):
    for b in range(1,10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == control_number:
                    counter += 1
                    is_combination_found = True
                    print(f"{a}{b}{c}{d} ", end="")
                if counter == 4:
                    is_password_find = True
                    password = str(a) + str(b) + str(c) + str(d)
                    counter += 1
print()
if not is_combination_found or not is_password_find:
    print("No!")
else:
    print(f"Password: {password}")