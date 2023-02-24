def move(crypted_text, letters_count_):
    left = crypted_text[letters_count_:len(crypted_text)]
    final_text = left + crypted_text[0:letters_count_]
    return final_text


def insert(crypted_text, index_, value_):
    left = crypted_text[0:index_] + value_
    final_text = left + crypted_text[index_:len(crypted_text)]
    return final_text


def change_all(crypted_text, substring_, replacement_):
    return crypted_text.replace(substring_, replacement_)


crypted_message = input()
command = input().split("|")

while command[0] != "Decode":
    if command[0] == "Move":
        letters_count = int(command[1])
        crypted_message = move(crypted_message, letters_count)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        crypted_message = insert(crypted_message, index, value)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        crypted_message = change_all(crypted_message, substring, replacement)

    command = input().split("|")
print(f"The decrypted message is: {crypted_message}")
