import re

text = input()
pattern = r"((?<=\s)[A-Za-z\d]+[\.\-\_]?[A-z\d]*@[A-z]+[\-]?[A-z]*(\.[A-z]+)+)"
result = re.findall(pattern, text)
for match in result:
    print(match[0])
