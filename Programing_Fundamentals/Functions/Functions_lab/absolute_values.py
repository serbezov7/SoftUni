numbers = list(map(float, input().split()))
new_list = []
for number in numbers:
    new_list.append(abs(number))
print(new_list)
