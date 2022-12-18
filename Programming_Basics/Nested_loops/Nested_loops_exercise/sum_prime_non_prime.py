command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0

while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
        command = input()
        continue
    count_numbers = 0

    for i in range(1, current_num + 1):
        if current_num % i == 0:
            count_numbers += 1
    if count_numbers == 2:
        sum_prime_numbers += current_num
    else:
        sum_non_prime_numbers += current_num
    command = input()
print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")