def contains(text_, substring_):
    if substring_ in text_:
        print(f"{text_} contains {substring}")
    else:
        print("Substring not found!")
    return text_


def flip_upper(text_, start_index_, end_index_):
    text_ = text[:start_index_] + text_[start_index_:end_index_].upper() + text_[end_index_:]
    print(text_)
    return text_


def flip_lower(text_, start_index_, end_index_):
    text_ = text[:start_index_] + text_[start_index_:end_index_].lower() + text_[end_index_:]
    print(text_)
    return text_


def slice_func(text_, start_index_, end_index_):
    text_ = text[:start_index_] + text_[end_index_:]
    print(text_)
    return text_


text = input()

command = input().split(">>>")


while command[0] != "Generate":
    if command[0] == "Contains":
        substring = command[1]
        text = contains(text, substring)
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            text = flip_upper(text, start_index, end_index)
        elif command[1] == "Lower":
            text = flip_lower(text, start_index, end_index)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        text = slice_func(text, start_index, end_index)

    command = input().split(">>>")

print(f"Your activation key is: {text}")