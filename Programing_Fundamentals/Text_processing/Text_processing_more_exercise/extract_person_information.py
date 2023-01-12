lines = int(input())

for line in range(lines):
    information = input()
    name = information[information.find("@") + 1:information.find("|")]
    age = information[information.find("#") + 1:information.find("*")]
    print(f"{name} is {age} years old.")


#
# lines = int(input())
#
# for line in range(lines):
#     information = input().split()
#     name = ""
#     years = ""
#     is_name = False
#     is_age = False
#     for index in range(len(information)):
#         if information[index].startswith("@"):
#             for letter in information[index]:
#                 if letter == "|":
#                     symbol_index = information[index].index(letter)
#                     name += information[index][1:symbol_index]
#                     is_name = True
#                     break
#
#         if information[index].startswith("#"):
#             for letter in information[index]:
#                 if letter == "*":
#                     symbol_index = information[index].index(letter)
#                     years += information[index][1:symbol_index]
#                     is_age = True
#                     break
#
#         if is_name and is_age:
#             print(f"{name} is {years} years old.")
#             is_name = False
#             is_age = False

