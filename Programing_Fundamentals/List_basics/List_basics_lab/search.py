lines = int(input())
searched_word = input()
my_list = []
filtered_list = []

for _ in range(lines):
    current_word = input()
    my_list.append(current_word)
    if searched_word in current_word:
        filtered_list.append(current_word)
print(my_list)
print(filtered_list)
