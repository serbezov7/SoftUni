numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    else:
        p5 += 1
p1_percent = p1 / numbers * 100
print(f"{p1_percent:.2f}%")
p2_percent = p2 / numbers * 100
print(f"{p2_percent:.2f}%")
p3_percent = p3 / numbers * 100
print(f"{p3_percent:.2f}%")
p4_percent = p4 / numbers * 100
print(f"{p4_percent:.2f}%")
p5_percent = p5 / numbers * 100
print(f"{p5_percent:.2f}%")