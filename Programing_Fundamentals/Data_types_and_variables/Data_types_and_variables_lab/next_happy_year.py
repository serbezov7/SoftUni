year = int(input())
happy_year_found = False

while not happy_year_found:
    year += 1
    set_year = set()
    for digit in range(len(str(year))):
        set_year.add(str(year)[digit])
    if len(set_year) == len(str(year)):
        happy_year_found = True
        print(year)
