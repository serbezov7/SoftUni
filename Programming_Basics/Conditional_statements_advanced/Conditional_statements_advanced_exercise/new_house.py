flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    price = 5
    if number_flowers > 80:
        price = price * 0.9
elif flowers == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        price = price * 0.85
elif flowers == "Tulips":
    price = 2.80
    if number_flowers > 80:
        price = price * 0.85
elif flowers == "Narcissus":
    price = 3.00
    if number_flowers < 120:
        price = price * 1.15
elif flowers == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        price = price * 1.2

total_price = number_flowers * price
difference = abs(total_price - budget)
if budget >= total_price:
    print(f"Hey, you have a great garden with {number_flowers} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
