number = int(input())
is_odd = False
for num in range(number):
    current_num = int(input())
    if current_num % 2 != 0:
        print(f"{current_num} is odd!")
        is_odd = True
        break
if not is_odd:
    print("All numbers are even.")