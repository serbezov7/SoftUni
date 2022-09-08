w = float(input())
h = float(input())
w_cent = w * 100
h_cent = h * 100 - 100

w_number = w_cent // 120
h_number = h_cent // 70

total_number = w_number * h_number - 3
print((total_number))
