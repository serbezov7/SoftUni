def swap(index1, index2, list_int):
    list_int[index1], list_int[index2] = list_int[index2], list_int[index1]


def multiply(index1, index2, list_int):
    list_int[index1] = list_int[index1] * list_int[index2]


def decrease(list_int):
    list_int = [x - 1 for x in list_int]
    # list_int = list(map(lambda x: x - 1, list_int))
    return list_int


initial_list = list(map(int, input().split()))
command = input().split()

while command[0] != "end":
    current_command = command[0]
    if current_command == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        swap(first_index, second_index, initial_list)
    elif current_command == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        multiply(first_index, second_index, initial_list)
    elif current_command == "decrease":
        initial_list = decrease(initial_list)
    command = input().split()
print(", ".join(str(x) for x in initial_list))
