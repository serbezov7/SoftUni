first_sequences = input().split(", ")
second_sequences = input().split(", ")
my_list = []

for current_word in first_sequences:
    for second_word in second_sequences:
        if current_word in second_word:
            my_list.append(current_word)
            break
print(my_list)

# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
# print(substrings)
