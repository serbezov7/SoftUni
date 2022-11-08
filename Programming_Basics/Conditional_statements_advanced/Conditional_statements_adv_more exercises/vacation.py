budget = float(input())
season = input()
place = ""
location = ""
price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:
        location = "Morocco"
        price = budget * 0.60
else:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    else:
        location = "Morocco"
        price = budget * 0.9
print(f"{location} - {place} - {price:.2f}")
