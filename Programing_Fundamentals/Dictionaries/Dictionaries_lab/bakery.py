elements = input().split()
my_dict = {}

for element in range(0, len(elements), 2):
    key = elements[element]
    value = int(elements[element + 1])
    my_dict[key] = value
print(my_dict)
