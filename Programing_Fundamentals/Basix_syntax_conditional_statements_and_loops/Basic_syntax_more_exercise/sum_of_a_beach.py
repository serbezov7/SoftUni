import re

word = input().lower()
pattern = r"fish|sand|water|sun"
matches = re.findall(pattern, word)
print(len(matches))


# if "Sand".lower() in word.lower():
#     counter += 1
# if "Water".lower() in word.lower():
#     counter += 1
# if "Fish".lower() in word.lower():
#     counter += 1
# if "Sun".lower() in word.lower():
#     counter += 1
# print(counter)
