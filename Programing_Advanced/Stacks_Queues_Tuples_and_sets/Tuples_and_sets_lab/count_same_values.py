numbers = [float(x) for x in input().split()]
my_dict = {}

for number in numbers:
    if number not in my_dict.keys():
        my_dict[number] = 0
    my_dict[number] += 1
for number, count in my_dict.items():
    print(f"{number:.1f} - {count} times")
    