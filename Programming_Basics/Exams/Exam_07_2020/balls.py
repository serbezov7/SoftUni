from math import floor
number = int(input())
total_points = 0
red_ball = 0
orange_ball = 0
yellow_ball = 0
white_ball = 0
black = 0
other = 0

for colors in range(number):
    current_color = input()
    if current_color == "red":
        total_points += 5
        red_ball += 1
    elif current_color == "orange":
        total_points += 10
        orange_ball += 1
    elif current_color == "yellow":
        total_points += 15
        yellow_ball += 1
    elif current_color == "white":
        total_points += 20
        white_ball += 1
    elif current_color == "black":
        total_points = floor(total_points / 2)
        black += 1
    else:
        other += 1
print(f"Total points: {total_points}")
print(f"Red balls: {red_ball}")
print(f"Orange balls: {orange_ball}")
print(f"Yellow balls: {yellow_ball}")
print(f"White balls: {white_ball}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")