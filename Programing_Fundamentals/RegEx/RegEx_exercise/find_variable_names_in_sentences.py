import re

text = input()
pattern = r"\b\_([A-Za-z0-9]+\b)"
result = re.findall(pattern, text)
print(",".join(result))
