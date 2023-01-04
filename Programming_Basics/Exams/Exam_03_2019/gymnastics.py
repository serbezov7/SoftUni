country = input()
device = input()
value = 0
if device == "ribbon":
    if country == "Russia":
        value = 9.100 + 9.400
    elif country == "Bulgaria":
        value = 9.600 + 9.400
    else:
        value = 9.200 + 9.500
elif device == "hoop":
    if country == "Russia":
        value = 9.300 + 9.800
    elif country == "Bulgaria":
        value = 9.550 + 9.750
    else:
        value = 9.450 + 9.350
else:
    if country == "Russia":
        value = 9.600 + 9.000
    elif country == "Bulgaria":
        value = 9.500 + 9.400
    else:
        value = 9.700 + 9.150
difference_percent = (20 - value) / 20 * 100
print(f"The team of {country} get {value:.3f} on {device}.")
print(f"{difference_percent:.2f}%")

