def range_character(first, second):
    list_characters = []
    for current_char in range(ord(first) + 1, ord(second)):
        list_characters.append(chr(current_char))
    return list_characters


first_character = input()
second_character = input()
result = range_character(first_character, second_character)
print(" ".join(result))
