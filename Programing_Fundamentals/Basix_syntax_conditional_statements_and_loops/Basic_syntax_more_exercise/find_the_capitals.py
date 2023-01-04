word = input()
word_list = []

for letter in range(len(word)):
    current_letter = word[letter]
    if current_letter.isupper():
        word_list.append(letter)
print(word_list)