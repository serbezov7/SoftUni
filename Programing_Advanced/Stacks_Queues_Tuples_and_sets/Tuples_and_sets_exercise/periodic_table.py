my_set = set()

for _ in range(int(input())):
    elements = input().split()
    for el in elements:
        my_set.add(el)
print("\n". join(my_set))
