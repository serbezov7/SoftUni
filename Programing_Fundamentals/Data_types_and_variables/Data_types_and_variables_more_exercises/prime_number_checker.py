number = int(input())
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
if is_prime:
    print("True")
else:
    print("False")