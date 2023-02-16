import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
result = re.finditer(pattern, text)
matches = []
counter = 0
if result:
    for match in result:
        counter += 1
        if match.groups()[1] == match.groups()[2][::-1]:
            matches.append(f"{match.groups()[1]} <=> {match.groups()[2]}")

    if counter == 0:
        print("No word pairs found!")

if counter > 0:
    print(f"{counter} word pairs found!")

if len(matches) > 0:
    print(f"The mirror words are:\n{', '.join(matches)}")
else:
    print("No mirror words!")
