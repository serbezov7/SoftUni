season = input()
kilometers = int(input())
salary = 0
if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = kilometers * 0.75
    elif season == "Summer":
        salary = kilometers * 0.9
    else:
        salary = kilometers * 1.05
elif kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = kilometers * 0.95
    elif season == "Summer":
        salary = kilometers * 1.10
    else:
        salary = kilometers * 1.25
elif kilometers <= 20000:
    salary = kilometers * 1.45

total_salary = salary * 4 * 0.9
print(f"{total_salary:.2f}")


