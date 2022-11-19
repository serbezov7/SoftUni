inherited_money = float(input())
year = int(input())
expenses = 0
age = 18
for years in range(1800, year + 1):
    if years % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 + (50 * age)
    age += 1
difference = abs(inherited_money - expenses)
if inherited_money >= expenses:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")

