lines = int(input())
last_char = ""
is_balanced = True

for line in range(lines):
    current_char = input()
    if current_char not in ["(", ")"]:
        continue
    if last_char == "" and current_char == ")" or last_char == current_char:
        is_balanced = False
        break
    last_char = current_char
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")