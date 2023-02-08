import re

text = input()
pattern = r"\=([A-Z][A-Za-z]{2,})\=|\/([A-Z][A-Za-z]{2,})\/"
result = re.finditer(pattern, text)
length = 0
towns = []
for match in result:
    if "=" in match.group():
        length += len(match.group(1))
        towns.append(match.group(1))
    elif "/" in match.group():
        length += len(match.group(2))
        towns.append(match.group(2))

print(f"Destinations: {', '.join(towns)}")
print(f"Travel Points: {length}")

# import re
#
# text = input()
# pattern = r"\=([A-Z][A-Za-z]{2,})\=|\/([A-Z][A-Za-z]{2,})\/"
# result = re.finditer(pattern, text)
# lenght = 0
# towns = []
# for match in result:
#     if "=" in match.group():
#         town = match.group().replace("=", "")
#         lenght += len(town)
#         towns.append(town)
#     elif "/" in match.group():
#         town = match.group().replace("/", "")
#         lenght += len(town)
#         towns.append(town)
#
# print(f"Destinations: {', '.join(towns)}")
# print(f"Travel Points: {lenght}")