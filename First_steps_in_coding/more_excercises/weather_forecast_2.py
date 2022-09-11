degrees = float(input())
if 26.00 <= degrees <= 35.00:
    print("Hot")
elif 20.10 <= degrees <= 25.90:
    print("Warm")
elif 15.00 <= degrees <= 20.00:
    print("Mild")
elif 12.00 <= degrees <= 14.99:
    print("Cool")
elif 5.00 <= degrees <= 11.90:
    print("Cold")
else:
    print("unknown")
