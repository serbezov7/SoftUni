from math import floor
import sys
command = input()
most_powerful_word = - sys.maxsize
word = ""

while command != "End of words":
    current_word = command
    sum_of_letters = 0

    for letter in current_word:
        sum_of_letters += ord(letter)
    if current_word[0] == "a" or current_word[0] == "A" or current_word[0] == "e" or current_word[0] == "E" or \
            current_word[0] == "i" or current_word[0] == "I" \
            or current_word[0] == "o" or current_word[0] == "O" or current_word[0] == "u" or current_word[0] == "U" or \
            current_word[0] == "y" or current_word[0] == "Y":
        sum_of_letters *= len(current_word)
    else:
        sum_of_letters /= floor(len(current_word))
    if sum_of_letters > most_powerful_word:
        most_powerful_word = sum_of_letters
        word = current_word
    command = input()
print(f"The most powerful word is {word} - {most_powerful_word}")