numbers = input().split("|")
flat_lis = []
for number in numbers[::-1]:
    flat_lis.extend(number.split())
print(*flat_lis)
