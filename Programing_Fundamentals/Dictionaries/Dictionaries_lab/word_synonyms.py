number_of_words = int(input())
synonym_dict = {}

for word in range(number_of_words):
    key = input()
    value = input()
    if key not in synonym_dict:
        synonym_dict[key] = [value]
    else:
        synonym_dict[key] += [value]  #.append(value)
for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")
