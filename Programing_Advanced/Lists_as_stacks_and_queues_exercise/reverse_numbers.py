initial_numbers = input().split()
my_stack = []

while initial_numbers:
    my_stack.append(initial_numbers.pop())

print(" ".join(my_stack))
