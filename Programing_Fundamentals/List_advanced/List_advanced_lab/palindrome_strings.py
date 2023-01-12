text = input().split()
palindrome = input()
palindrome_list = [x for x in text if x == x[::-1]]
palindrome_counter = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
