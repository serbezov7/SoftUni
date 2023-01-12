to_remove = input()
string = input()

while to_remove in string:
    string = string.replace(to_remove, "")
print(string)