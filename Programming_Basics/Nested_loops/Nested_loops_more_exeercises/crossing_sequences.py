tribonacci_first_num = int(input())
tribonacci_second_num = int(input())
tribonacci_third_num = int(input())
spiral_initial = int(input())
spiral_step = int(input())

tribonacci_numbers = [tribonacci_first_num, tribonacci_second_num, tribonacci_third_num]

tribonacci_current = tribonacci_third_num

while tribonacci_current <= 1000000:
    tribonacci_current = tribonacci_first_num + tribonacci_second_num + tribonacci_third_num
    tribonacci_numbers.append(tribonacci_current)

    tribonacci_first_num = tribonacci_second_num
    tribonacci_second_num = tribonacci_third_num
    tribonacci_third_num = tribonacci_current

spiral_numbers = [spiral_initial]
spiral_multiplier = 1
counter = 0
spiral_current = spiral_initial

while spiral_current <= 1000000:
    spiral_current += spiral_step * spiral_multiplier
    spiral_numbers.append(spiral_current)
    counter += 1

    if counter % 2 == 0:
        spiral_multiplier += 1

is_found = False

for i in range(len(tribonacci_numbers)):
    for j in range(len(spiral_numbers)):
        if tribonacci_numbers[i] == spiral_numbers[j] and tribonacci_numbers[i] <= 1000000:
            print(tribonacci_numbers[i])
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print("No")