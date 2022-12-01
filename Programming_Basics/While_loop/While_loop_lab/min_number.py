import sys
command = input()
min_number = sys.maxsize

while command != "Stop":
    current_num = int(command)
    if current_num < min_number:
        min_number = current_num
    command = input()
print(min_number)