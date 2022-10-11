fruit = input()
day_of_the_week = input()
quantity = float(input())
price = 0
valid_day_of_the_week = True
valid_fruit = True

if day_of_the_week == "Monday" \
    or day_of_the_week == "Tuesday" \
    or day_of_the_week == "Wednesday" \
    or day_of_the_week == "Thursday" \
    or day_of_the_week == "Friday":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        valid_fruit = False
elif day_of_the_week == "Saturday" \
    or day_of_the_week == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        valid_fruit = False
else:
    valid_day_of_the_week = False
if valid_day_of_the_week and valid_fruit: # if valid_fruit == True and valid_day_of_the_week == True:
    total_price = price * quantity
    print(f"{total_price:.2f}")
else:
    print("error")


