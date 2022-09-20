x_high = float(input())
y_lenght = float(input())
h_triangle_side = float(input())

side_wall = x_high * y_lenght
window = 1.5 ** 2
total_side_wall = 2 * side_wall - 2 * window
back_wall = x_high ** 2
entrance = 1.2 * 2
total_front_back = total_side_wall + back_wall * 2 - entrance
roof = x_high * y_lenght * 2
roof_triangle = 2 * (x_high * h_triangle_side / 2)
total_roof = roof + roof_triangle
red_paint = total_roof / 4.3
green_paint = total_front_back / 3.4

print("{:.2f}".format(green_paint))
print("{:.2f}".format(red_paint))
