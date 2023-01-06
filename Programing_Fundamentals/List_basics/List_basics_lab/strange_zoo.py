my_list = []

for _ in range(3):
    body_part = input()
    my_list.append(body_part)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
