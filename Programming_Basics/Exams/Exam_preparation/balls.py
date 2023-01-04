number_of_balls = int(input())
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0
total_points = 0

for color in range(number_of_balls):
    current_ball_color = input()
    if current_ball_color == "red":
        red_balls += 1
        total_points += 5
    elif current_ball_color == "orange":
        orange_balls += 1
        total_points += 10
    elif current_ball_color == "yellow":
        yellow_balls += 1
        total_points += 15
    elif current_ball_color == "white":
        white_balls += 1
        total_points += 20
    elif current_ball_color == "black":
        black_balls += 1
        total_points //= 2
    else:
        other_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")