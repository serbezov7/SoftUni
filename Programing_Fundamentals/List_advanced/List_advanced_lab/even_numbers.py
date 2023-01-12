numbers = list(map(int, input().split(", ")))
indices = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]
print(indices)