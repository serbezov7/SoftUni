budget = float(input())
season = input()
car_class = ""
type_car = ""
price = 0
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    else:
        type_car = "Jeep"
        price = budget * 0.65

elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    else:
        type_car = "Jeep"
        price = budget * 0.80
else:
    car_class = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.90
print(car_class)
print(f"{type_car} - {price:.2f}")