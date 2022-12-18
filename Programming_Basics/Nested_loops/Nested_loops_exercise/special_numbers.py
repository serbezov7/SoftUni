number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if number % i == 0 and number % j == 0 and number % k == 0 and number % l == 0:
                    print(f"{i}{j}{k}{l}", end=" ")

# number = int(input())
# number_to_print = ""
#
# for i in range(1111, 10000):
#     string_i = str(i)
#     for symbol in range(len(string_i)):
#         digit = int(string_i[symbol])
#         if digit != 0:
#             if number % digit == 0:
#                 str_number = str(digit)
#                 number_to_print += str_number
#     if len(number_to_print) == 4:
#         print(number_to_print, end=" ")
#     number_to_print = ""


