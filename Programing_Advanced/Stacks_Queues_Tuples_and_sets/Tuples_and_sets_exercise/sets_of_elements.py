n, m = [int(x) for x in input().split()]

first_set = set(int(input()) for _ in range(n))
second_set = set(int(input()) for _ in range(m))

match_elements = first_set.intersection(second_set)
print(*match_elements, sep="\n")
