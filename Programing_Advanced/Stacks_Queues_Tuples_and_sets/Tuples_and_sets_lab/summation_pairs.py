numbers = [int(x) for x in input().split()]
target_number = int(input())
my_set = set()
my_dict = {}

for number in numbers:
    if number in my_dict.keys():
        my_set.remove(my_dict[number])
        second_num = my_dict[number]
        del my_dict[number]
        print(f"{second_num} + {number} = {target_number}")
    else:
        my_set.add(number)
        difference = target_number - number
        my_dict[difference] = number
