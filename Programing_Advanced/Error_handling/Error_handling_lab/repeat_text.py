text = input()
try:
    repeat_times = int(input())
    print(text * repeat_times)
except ValueError:
    print("Variable times must be integer")