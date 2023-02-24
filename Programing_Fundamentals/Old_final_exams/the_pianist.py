def add(pieces_dict_, piece_, compositor_, key_):
    if piece_ in pieces_dict_.keys():
        print(f"{piece_} is already in the collection!")
    else:
        pieces_dict_[piece_] = {key_: compositor_}
        print(f"{piece_} by {compositor_} in {key_} added to the collection!")
    return pieces_dict_


def remove(pieces_dict_, piece_):
    if piece_ in pieces_dict_.keys():
        del pieces_dict_[piece_]
        print(f"Successfully removed {piece_}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    return pieces_dict_


def change_key(pieces_dict_, piece_, new_key_):
    compositor = ""
    pieces_key = ""
    if piece_ in pieces_dict_.keys():
        for key, value in pieces_dict_[piece_].items():
            compositor += value
            pieces_key += key
        del pieces_dict_[piece_][pieces_key]
        pieces_dict_[piece_] = {new_key_: compositor}
        print(f"Changed the key of {piece_} to {new_key_}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    return pieces_dict_


pieces = int(input())
pieces_dict = {}

for _ in range(pieces):
    piece, compositor, key = input().split("|")
    pieces_dict[piece] = {key: compositor}
command = input().split("|")

while command[0] != "Stop":
    if command[0] == "Add":
        piece = command[1]
        compositor = command[2]
        key = command[3]
        pieces_dict = add(pieces_dict, piece, compositor, key)
    elif command[0] == "Remove":
        piece = command[1]
        pieces_dict = remove(pieces_dict, piece)
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        pieces_dict = change_key(pieces_dict, piece, new_key)

    command = input().split("|")

for key in pieces_dict.keys():
    for key_, value in pieces_dict[key].items():
        print(f"{key} -> Composer: {value}, Key: {key_}")
