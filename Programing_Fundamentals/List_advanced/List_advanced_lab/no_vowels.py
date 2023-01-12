text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = [x for x in text if not x.lower() in vowels]
print("".join(no_vowels))

