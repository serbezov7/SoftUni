import re
text = input()
pattern = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})\1"
pattern_digit = r"\d"
result = re.finditer(pattern, text)
result_digit = re.finditer(pattern_digit, text)

emoji_counter = 0
cool_treshhold = 1
cools_emojis = []

for match in result_digit:
    if match.group().isdigit():
        cool_treshhold *= int(match.group())

for match in result:
    coolness = 0
    for letter in match.group():
        if letter.isalpha():
            coolness += ord(letter)
    emoji_counter += 1
    if coolness > cool_treshhold:
        cools_emojis.append(match.group())

print(f"Cool threshold: {cool_treshhold}")
n1 = "\n"
print(f"{emoji_counter} emojis found in the text. The cool ones are:{n1}{n1.join(cools_emojis)}")
