first_pair_start = int(input())
second_pair_start = int(input())
first_stop = int(input())
second_stop = int(input())
non_prime = False

for i in range(first_pair_start, first_pair_start + first_stop + 1):
    for j in range(second_pair_start, second_pair_start + second_stop + 1):
        for k in range(2, i):
            for l in range(2, j):
                if i % k == 0 or j % l == 0:
                    non_prime = True
        if not non_prime:
            print(f"{i}{j}")
        non_prime = False