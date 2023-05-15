# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("That was not a valid number, please try again")

# try:
#     x = int("Peter")
# except ValueError:
#     print("Cannot convert int to str")
# finally:
#     print("This is finally")

try:
    x = int(input())
except ValueError as error:
    print(error)