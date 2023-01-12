import re

text = input()
searched_word = input()
pattern = fr"(?i){searched_word}\b"
result = re.findall(pattern, text)
print(len(result))