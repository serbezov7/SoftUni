numbers = input().split()
initial_message = input()
final_message = []

for number in numbers:
    sum_number = 0
    for i in number:
        sum_number += int(i)
    index = sum_number % len(initial_message)
    final_message.append(initial_message[index])
    initial_message = initial_message.replace(initial_message[index], "", 1)
print("".join(final_message))

