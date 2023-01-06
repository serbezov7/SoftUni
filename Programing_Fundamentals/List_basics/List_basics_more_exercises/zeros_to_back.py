list_numbers = list(map(int, input().split(", ")))

for number in list_numbers:
    list_numbers.append(list_numbers.pop(list_numbers.index(0)))
print(list_numbers)



#     if number == 0:
#         list_numbers.insert(len(list_numbers), list_numbers.pop(list_numbers.index(0)))
# print(list_numbers)
