first_number_range = int(input())
second_number_range = int(input())
third_number_range = int(input())
non_prime = False

for i in range(1, first_number_range + 1):
    for j in range(2, second_number_range + 1):
        for k in range(1, third_number_range + 1):
            if i % 2 == 0 and k % 2 == 0:
                for fourth in range(2, j):
                    if j % fourth == 0:
                        non_prime = True
                if not non_prime:
                    print(f"{i} {j} {k}")
                non_prime = False