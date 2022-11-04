season = input()
group = input()
count_students = int(input())
nights = int(input())
price = 0
sport = ""

if group == "boys" or group == "girls":
    if season == "Winter":
        price = count_students * 9.60 * nights
    elif season == "Spring":
        price = count_students * 7.20 * nights
    else:
        price = count_students * 15 * nights
else:
    if season == "Winter":
        price = count_students * 10 * nights
    elif season == "Spring":
        price = count_students * 9.50 * nights
    else:
        price = count_students * 20 * nights

if count_students >= 50:
    price *= 0.5
elif 20 <= count_students < 50:
    price *= 0.85
elif 10 <= count_students < 20:
    price *= 0.95

if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
    elif group == "boys":
        sport = "Judo"
    else:
        sport = "Ski"
elif season == "Spring":
    if group == "girls":
        sport = "Athletics"
    elif group == "boys":
        sport = "Tennis"
    else:
        sport = "Cycling"
else:
    if group == "girls":
        sport = "Volleyball"
    elif group == "boys":
        sport = "Football"
    else:
        sport = "Swimming"
print(f"{sport} {price:.2f} lv.")
