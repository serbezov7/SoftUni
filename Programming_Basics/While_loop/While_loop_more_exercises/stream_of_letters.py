import string

command = input()
secret_word = ""
current_word = ""
c = 0
o = 0
n = 0

while command != "End":
    if command in string.ascii_lowercase or command in string.ascii_uppercase:
        if command == "c":
            c += 1
            if c > 1:
                current_word += command
        elif command == "o":
            o += 1
            if o > 1:
                current_word += command
        elif command == "n":
            n += 1
            if n > 1:
                current_word += command
        else:
            current_word += command
        if c >= 1 and o >= 1 and n >= 1:
            secret_word += current_word + " "
            current_word = ''
            c = 0
            o = 0
            n = 0
    else:
        pass
    command = input()
print(secret_word)