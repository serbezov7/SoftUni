command = input()
kids = 0
adults = 0
money_toys = 0
money_sweaters = 0
while command != "Christmas":
    person_year = int(command)
    if person_year <= 16:
        kids += 1
        money_toys += 5
    else:
        adults += 1
        money_sweaters += 15
    command = input()
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {money_sweaters}")
