def merge(start, end, text):
    if start < 0:
        start = 0
    if end > len(text) - 1:
        end = len(text) - 1
    for index in range(start, end):
        text[start] += text.pop(start + 1)


def divide(index_, partitions_, text):
    element = text.pop(index_)
    step = len(element) // partitions_
    for word in range(partitions_ - 1):
        text.insert(index_, element[:step])
        element = element[step:]
        index_ += 1
    text.insert(index_, element)


input_text = input().split()
command = input().split()

while command[0] != "3:1":
    current_command = command[0]
    if current_command == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        merge(start_index, end_index, input_text)
    elif current_command == "divide":
        index = int(command[1])
        partitions = int(command[2])
        divide(index, partitions, input_text)

    command = input().split()
print(" ".join(input_text))




# text = input().split()
# command = input().split()
#
# while command[0] != "3:1":
#     current_command = command[0]
#     if current_command == "merge":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         if start_index < 0:
#             start_index = 0
#         if end_index > len(text) - 1:
#             end_index = len(text) - 1
#         for index, string in enumerate(text):
#             if index in range(start_index + 1, end_index + 1):
#                 text[start_index] += text[index]
#         for index in range(end_index, start_index, - 1):
#             text.pop(index)
#     elif current_command == "divide":
#         index = int(command[1])
#         partitions = int(command[2])
#         if partitions > len(text[index]):
#             step = 1
#         else:
#             step = len(text[index]) // partitions
#             removed_part = text.pop(index)
#             start = 0
#             for parts in range(partitions):
#                 if parts == partitions - 1:
#                     text.insert(index, removed_part[start:])
#                 else:
#                     text.insert(index, removed_part[start:start + step])
#                     start += step
#                     index += 1
#     command = input().split()
#
# print(" ".join(text))
