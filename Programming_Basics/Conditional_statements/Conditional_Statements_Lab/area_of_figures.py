from math import pi

figure = input()
result = 0
if figure == "square":
    side = float(input())
    result = side ** 2
elif figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif figure == "circle":
    radius = float(input())
    result = pi * radius ** 2
else:
    side_a = float(input())
    h = float(input())
    result = side_a * h / 2
print(f"{result:.3f}")