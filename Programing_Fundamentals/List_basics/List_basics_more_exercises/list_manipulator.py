initial_list = list(map(int, input().split()))
command = input().split()

while command[0] != "end":
    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(initial_list):
            first_list = initial_list[index + 1:]
            second_list = initial_list[:index + 1]
            initial_list = first_list + second_list
        else:
            print("Invalid index")
    elif command[0] == "max":
        if command[1] == "even":
            new_list = max([x for x in initial_list if x % 2 == 0], default=-1)
            if new_list == -1:
                print("No matches")
            else:
                right_index = 0
                for index, value in enumerate(initial_list):
                    if value == new_list and index > right_index:
                        right_index = index
                print(right_index)
        elif command[1] == "odd":
            new_list = max([x for x in initial_list if x % 2 != 0], default=-1)
            if new_list == -1:
                print("No matches")
            else:
                right_index = 0
                for index, value in enumerate(initial_list):
                    if value == new_list and index > right_index:
                        right_index = index
                print(right_index)
    elif command[0] == "min":
        if command[1] == "even":
            new_list = min([x for x in initial_list if x % 2 == 0], default=-1)
            if new_list == -1:
                print("No matches")
            else:
                right_index = 0
                for index, value in enumerate(initial_list):
                    if value == new_list and index > right_index:
                        right_index = index
                print(right_index)
        elif command[1] == "odd":
            new_list = min([x for x in initial_list if x % 2 != 0], default=-1)
            if new_list == -1:
                print("No matches")
            else:
                right_index = 0
                for index, value in enumerate(initial_list):
                    if value == new_list and index > right_index:
                        right_index = index
                print(right_index)
    elif command[0] == "first":
        count = int(command[1])
        if count <= len(initial_list):
            if command[2] == "even":
                new_list = [x for x in initial_list if x % 2 == 0][:count]
                print(new_list)
            elif command[2] == "odd":
                new_list = [x for x in initial_list if x % 2 != 0][:count]
                print(new_list)
        else:
            print("Invalid count")
    elif command[0] == "last":
        count = int(command[1])
        if count <= len(initial_list):
            if command[2] == "even":
                new_list = [x for x in initial_list if x % 2 == 0]
                if count > len(new_list):
                    count = len(new_list)
                new_list = new_list[len(new_list) - count:]
                print(new_list)
            elif command[2] == "odd":
                new_list = [x for x in initial_list if x % 2 != 0]
                if count > len(new_list):
                    count = len(new_list)
                new_list = new_list[len(new_list) - count:]
                print(new_list)
        else:
            print("Invalid count")

    command = input().split()
print(initial_list)

# initial_list = list(map(int, input().split()))
# command = input().split()
#
# while command[0] != "end":
#     if command[0] == "exchange":
#         index = int(command[1])
#         if 0 <= index < len(initial_list):
#             first_list = initial_list[index + 1:]
#             second_list = initial_list[:index + 1]
#             initial_list = first_list + second_list
#         else:
#             print("Invalid index")
#     elif command[0] == "max":
#         if command[1] == "even":
#             right_index = "No matches"
#             if [x for x in initial_list if x % 2 == 0]:
#                 right_index = 0
#                 new_list = max([x for x in initial_list if x % 2 == 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#         elif command[1] == "odd":
#             if [x for x in initial_list if x % 2 != 0]:
#                 right_index = 0
#                 new_list = max([x for x in initial_list if x % 2 != 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#     elif command[0] == "min":
#         if command[1] == "even":
#             if [x for x in initial_list if x % 2 == 0]:
#                 right_index = 0
#                 new_list = min([x for x in initial_list if x % 2 == 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#         elif command[1] == "odd":
#             if [x for x in initial_list if x % 2 != 0]:
#                 right_index = 0
#                 new_list = min([x for x in initial_list if x % 2 != 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#     elif command[0] == "first":
#         count = int(command[1])
#         if 0 <= count <= len(initial_list):
#             if command[2] == "even":
#                 new_list = [x for x in initial_list if x % 2 == 0][:count]
#                 print(new_list)
#             elif command[2] == "odd":
#                 new_list = [x for x in initial_list if x % 2 != 0][:count]
#                 print(new_list)
#         else:
#             print("Invalid count")
#     elif command[0] == "last":
#         count = int(command[1])
#         if 0 <= count <= len(initial_list):
#             if command[2] == "even":
#                 new_list = [x for x in initial_list if x % 2 == 0]
#                 if count > len(new_list):
#                     count = len(new_list)
#                 new_list = new_list[len(new_list) - count:]
#                 print(new_list)
#             elif command[2] == "odd":
#                 new_list = [x for x in initial_list if x % 2 != 0]
#                 if count > len(new_list):
#                     count = len(new_list)
#                 new_list = new_list[len(new_list) - count:]
#                 print(new_list)
#         else:
#             print("Invalid count")
#
#     command = input().split()
# print(initial_list)


# initial_list = list(map(int, input().split()))
# command = input().split()
#
# while command[0] != "end":
#     if command[0] == "exchange":
#         index = int(command[1])
#         if 0 <= index < len(initial_list):
#             first_list = initial_list[index + 1:]
#             second_list = initial_list[:index + 1]
#             initial_list = first_list + second_list
#         else:
#             print("Invalid index")
#     elif command[0] == "max":
#         if command[1] == "even":
#             right_index = "No matches"
#             if [x for x in initial_list if x % 2 == 0]:
#                 right_index = 0
#                 new_list = max([x for x in initial_list if x % 2 == 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#         elif command[1] == "odd":
#             if [x for x in initial_list if x % 2 != 0]:
#                 right_index = 0
#                 new_list = max([x for x in initial_list if x % 2 != 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#     elif command[0] == "min":
#         if command[1] == "even":
#             if [x for x in initial_list if x % 2 == 0]:
#                 right_index = 0
#                 new_list = min([x for x in initial_list if x % 2 == 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#         elif command[1] == "odd":
#             if [x for x in initial_list if x % 2 != 0]:
#                 right_index = 0
#                 new_list = min([x for x in initial_list if x % 2 != 0])
#                 for index, value in enumerate(initial_list):
#                     if value == new_list and index > right_index:
#                         right_index = index
#                 print(right_index)
#             else:
#                 print("No matches")
#     elif command[0] == "first":
#         count = int(command[1])
#         if count <= len(initial_list):
#             if command[2] == "even":
#                 print([x for x in initial_list if x % 2 == 0][:count])
#             elif command[2] == "odd":
#                 print([x for x in initial_list if x % 2 != 0][:count])
#
#         else:
#             print("Invalid count")
#     elif command[0] == "last":
#         count = int(command[1])
#         if count <= len(initial_list):
#             if command[2] == "even":
#                 print(list(reversed([x for x in reversed(initial_list) if x % 2 == 0][:count])))
#             elif command[2] == "odd":
#                 print(list(reversed([x for x in reversed(initial_list) if x % 2 != 0][:count])))
#         else:
#             print("Invalid count")
#
#     command = input().split()
# print(initial_list)
