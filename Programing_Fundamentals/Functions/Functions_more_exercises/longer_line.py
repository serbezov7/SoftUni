from math import floor


def center_point(x1, y1, x2, y2, x3, y3, x4, y4):
    total_sum_first = abs(x1) + abs(y1) + abs(x2) + abs(y2)
    first_sum_x = abs(x1) + abs(y1)
    second_sum_x = abs(x2) + abs(y2)
    total_sum_second = abs(x3) + abs(y3) + abs(x4) + abs(y4)
    first_sum_y = abs(x3) + abs(y3)
    second_sum_y = abs(x4) + abs(y4)
    if total_sum_first >= total_sum_second:
        if first_sum_x <= second_sum_x:
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    else:
        if first_sum_y <= second_sum_y:
            return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            return f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"


first = float(input())
second = float(input())
third = float(input())
fourth = float(input())
fifth = float(input())
sixth = float(input())
seventh = float(input())
eight = float(input())
print(center_point(first, second, third, fourth, fifth, sixth, seventh, eight))

