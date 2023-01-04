from math import ceil, floor

n = int(input())

if n <= 2:
    print("*" * n)
else:
    outside = ceil(n - 2) / 2
    inside = 0
    if n % 2 == 0:
        for row in range(1, ceil(n / 2) + 1):
            print("-" * int(outside) + "*" + "-" * int(inside) + "*" + "-" * int(outside))
            outside -= 1
            inside += 2
        outside += 1
        inside -= 2
        for row in range(1, ceil(n / 2)):
            inside -= 2
            outside += 1
            print("-" * int(outside) + "*" + "-" * int(inside) + "*" + "-" * int(outside))

    else:
        for row in range(1, floor(n / 2) + 2):
            if row == 1:
                print("-" * ceil(outside) + "*" + "-" * ceil(outside))
            else:
                inside += 1
                outside -= floor(1)
                print("-" * ceil(outside) + "*" + "-" * ceil(inside) + "*" + "-" * ceil(outside))
                inside += 1
        inside -= 1
        for row in range(1, floor(n / 2) + 1):
            inside -= 2
            outside += 1
            if row == floor(n / 2):
                print("-" * ceil(outside) + "*" + "-" * ceil(inside) + "-" * ceil(outside))
            else:
                print("-" * ceil(outside) + "*" + "-" * ceil(inside) + "*" + "-" * ceil(outside))
