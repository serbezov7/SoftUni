number = (input())
final_number = []
for num in range(len(number)):
    new_number = number[num]
    final_number.append(new_number)
final_number.sort(reverse=True)
print("".join(final_number))
