factor = int(input())
count = int(input())

my_list = []
for multiplayer in range(1, count + 1):
    my_list.append(factor * multiplayer)
print(my_list)