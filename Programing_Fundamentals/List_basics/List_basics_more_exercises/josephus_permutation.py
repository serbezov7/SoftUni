list_of_people = input().split()
count = int(input())
new_list = []
counter = 0
index = 0
while len(list_of_people) > 0:
    counter += 1
    if counter % count == 0:
        new_list.append(list_of_people.pop(index))
    else:
        index += 1
    if index == len(list_of_people):
        index = 0
print(str(new_list).replace(" ", "").replace("\'", ""))
