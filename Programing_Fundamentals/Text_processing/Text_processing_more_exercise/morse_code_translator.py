code = input().split(" | ")
morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

deciphered_code = ""
for word in code:
    word = word.split()
    is_found = False
    for current_word in range(len(word)):
        for key, value in morse_code_dict.items():
            if word[0] == value:
                deciphered_code += key
                word.remove(word[0])
                is_found = True
                break
        if is_found and len(word) == 0:
            deciphered_code += " "
            break
print(deciphered_code)
