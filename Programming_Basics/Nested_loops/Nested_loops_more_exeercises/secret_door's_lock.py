first_end = int(input())
second_end = int(input())
third_end = int(input())
non_prime = False
for i in range(1, first_end + 1):
    for j in range(2, second_end + 1):
        for k in range(1, third_end + 1):
            if i % 2 == 0 and k % 2 == 0:
                for l in range(2, j):
                    if j % l == 0:
                        non_prime = True
                if not non_prime:
                    print(f"{i} {j} {k}")
                non_prime = False

