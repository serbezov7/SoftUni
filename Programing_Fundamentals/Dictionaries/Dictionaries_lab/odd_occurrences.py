words = input().lower().split()
words_dictionary = {}

for word in words:
    if word not in words_dictionary:
        words_dictionary[word] = 0
    words_dictionary[word] += 1
new_dict = {key: value for key, value in words_dictionary.items() if value % 2 != 0}
print(" ".join(new_dict.keys()))
