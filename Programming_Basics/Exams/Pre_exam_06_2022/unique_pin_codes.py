first_num = int(input())
second_num = int(input())
third_num = int(input())

for num1 in range(2, first_num + 1):
    for num2 in range(2, second_num + 1):
        for num3 in range(2, third_num + 1):
            if num1 % 2 == 0 and num3 % 2 == 0 and (num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7):
                print(f"{num1} {num2} {num3}")