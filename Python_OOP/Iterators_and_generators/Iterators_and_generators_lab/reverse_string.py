def reverse_text(string):
    for letter in reversed(string):
        yield letter


for char in reverse_text("step"):
    print(char, end='')