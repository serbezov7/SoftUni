first_name, second_name = input().split()
total_sum = 0
if len(first_name) > len(second_name):
    for index in range(len(second_name)):
        total_sum += ord(first_name[index]) * ord(second_name[index])
    for index in range(len(second_name), len(first_name)):
        total_sum += ord(first_name[index])
elif len(first_name) < len(second_name):
    for index in range(len(first_name)):
        total_sum += ord(first_name[index]) * ord(second_name[index])
    for index in range(len(first_name), len(second_name)):
        total_sum += ord(second_name[index])
else:
    for index in range(len(first_name)):
        total_sum += ord(first_name[index]) * ord(second_name[index])

print(total_sum)