import re

pattern = r"(w{3}\.([A-Za-z0-9]+)([\-A-Za-z0-9]+)*([\.][a-z]+)+)"
text = input()
while text:
    result = re.findall(pattern, text)
    if result:
        print(result[0][0])

    text = input()