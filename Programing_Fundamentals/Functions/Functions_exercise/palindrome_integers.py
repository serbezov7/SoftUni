def is_palindrome(num):
    for current_num in num:
        if current_num == current_num[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")
is_palindrome(numbers)
