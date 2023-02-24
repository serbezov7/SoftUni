lines = int(input())
my_stack = []

mapper = {
    "1": lambda x: my_stack.append(int(x[1])),
    "2": lambda x: my_stack.pop() if my_stack else None,
    "3": lambda x: print(max(my_stack)) if my_stack else None,
    "4": lambda x: print(min(my_stack)) if my_stack else None,
}

for line in range(lines):
    command = input().split()
    mapper[command[0]](command)

my_stack.reverse()
print(*my_stack, sep=", ")

# lines = int(input())
# my_stack = []
#
# for line in range(lines):
#     command = input().split()
#     if command[0] == "1":
#         number = int(command[1])
#         my_stack.append(number)
#     elif command[0] == "2":
#         if my_stack:
#             my_stack.pop()
#     elif command[0] == "3":
#         if my_stack:
#             print(max(my_stack))
#     elif command[0] == "4":
#         if my_stack:
#             print(min(my_stack))
#
# my_stack.reverse()
# print(*my_stack, sep=", ")
