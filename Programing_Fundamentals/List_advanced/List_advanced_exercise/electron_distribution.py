def check_electrons(electrons):
    position = 1
    while electrons > 0:
        max_electrons = 2 * position ** 2
        if electrons >= max_electrons:
            filled_shells.append(max_electrons)
            electrons -= max_electrons
        elif electrons <= max_electrons:
            filled_shells.append(electrons)
            electrons -= max_electrons
        position += 1


electrons_input = int(input())
filled_shells = []
check_electrons(electrons_input)
print(filled_shells)
