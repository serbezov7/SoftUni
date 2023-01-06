lines = int(input())
my_list = []
filtered_list = []

for _ in range(lines):
    current_number = int(input())
    my_list.append(current_number)

command = input()
for number in my_list:
    if command == "even" and number % 2 == 0 \
            or command == "odd" and number % 2 != 0 \
            or command == "negative" and number < 0 \
            or command == "positive" and number >= 0:
        filtered_list.append(number)
print(filtered_list)
