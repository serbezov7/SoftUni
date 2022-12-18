start_number = int(input())
finish_number = int(input())

for number in range(start_number, finish_number + 1):
    string_number = str(number)
    odd_sum = 0
    even_sum = 0
    for symbol in range(len(string_number)):
        digit = int(string_number[symbol])
        if symbol % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if odd_sum == even_sum:
        print(number, end=" ")

# start_number = int(input())
# finish_number = int(input())
#
# for num in range(start_number, finish_number + 1):
#     str_num = str(num)
#
#     sixth_num = 0
#     fifth_num = 0
#     fourth_num = 0
#     third_num = 0
#     second_num = 0
#     first_num = 0
#     odd_sum = 0
#     even_sum = 0
#
#     for j in range(len(str_num)):
#         str_num = int(str_num)
#
#         current_num = str_num % 10
#         if j == 0:
#             sixth_num = current_num
#         elif j == 1:
#             fifth_num = current_num
#         elif j == 2:
#             fourth_num = current_num
#         elif j == 3:
#             third_num = current_num
#         elif j == 4:
#             second_num = current_num
#         else:
#             first_num = current_num
#         str_num = str_num // 10
#         even_sum = second_num + fourth_num + sixth_num
#         odd_sum = first_num + third_num + fifth_num
#     if even_sum == odd_sum:
#         print(num, end=" ")
