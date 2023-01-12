strings = input().split()

for word in strings:
    print(word * len(word), end="")

# print("".join(word * len(word) for word in input().split()))