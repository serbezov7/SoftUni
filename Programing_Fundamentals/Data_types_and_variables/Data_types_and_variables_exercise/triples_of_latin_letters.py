letters = int(input())

for letter in range(letters):
    for second_letter in range(letters):
        for third_letter in range(letters):
            print(chr(97 + letter) + chr(97 + second_letter) + chr(97 + third_letter))
