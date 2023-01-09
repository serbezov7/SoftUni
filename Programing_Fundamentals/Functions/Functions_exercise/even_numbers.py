def is_even(num):
    return num % 2 == 0


number = list(map(int, input().split()))
even_numbers = list(filter(is_even, number))
print(even_numbers)
