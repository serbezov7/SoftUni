list_numbers = list(map(int, input().split()))
total_sum = 0

for number in list_numbers:
    total_sum += number
average = (total_sum / len(list_numbers))
if max(list_numbers) > average:
    list_numbers = sorted([x for x in list_numbers if x > average], reverse=True)
    if len(list_numbers) >= 5:
        list_numbers = [list_numbers[x] for x in range(5)]
    else:
        list_numbers = [list_numbers[x] for x in range(len(list_numbers))]
    print(" ".join(str(x) for x in list_numbers))
else:
    print("No")
