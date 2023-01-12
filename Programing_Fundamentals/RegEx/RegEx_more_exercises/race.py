import re

participants = input().split(", ")
pattern = r"[A-Za-z]+|\d"
score_dict = {}
command = input()

while command != "end of race":
    result = re.findall(pattern, command)
    name = ""
    digits = []
    for char in result:
        if char.isalpha():
            name += char
        elif char.isdigit():
            digits.append(int(char))
    if name in participants:
        if name in score_dict.keys():
            score_dict[name] += sum(digits)
        else:
            score_dict[name] = sum(digits)

    command = input()
score_dict = sorted(score_dict.items(), key=lambda x: -x[1])

counter = 1
for ranking in range(0, 3):
    if counter == 1:
        print(f"{counter}st place: {score_dict[ranking][0]}")
    elif counter == 2:
        print(f"{counter}nd place: {score_dict[ranking][0]}")
    else:
        print(f"{counter}rd place: {score_dict[ranking][0]}")
    counter += 1
