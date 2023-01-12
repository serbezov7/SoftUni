some_text = input()
new_text = ""

for letter in some_text:
    new_text += chr(ord(letter) + 3)

print(new_text)