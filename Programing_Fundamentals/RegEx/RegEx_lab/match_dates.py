import re
text = input()
pattern = r"(\d{2})([/.-])([A-Z]{1}[a-z]{2})\2(\d{4})"
result = re.finditer(pattern, text)
for match in result:
    print(f"Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}", )
# result = re.findall(pattern, text)
# for match in result:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}", )