budget = float(input())
season = input()
destination = ""
price = 0
place = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = budget * 0.3
    elif season == "winter":
        price = budget * 0.7
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = budget * 0.4
    elif season == "winter":
        place = "Hotel"
        price = budget * 0.8
else:
    destination = "Europe"
    price = budget * 0.9
    place = "Hotel"
print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")


