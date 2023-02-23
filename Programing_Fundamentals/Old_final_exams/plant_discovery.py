def rate(plants_dict_, plant_, rating_):
    if plant_ in plants_dict_.keys():
        plants_dict_[plant_]["rating"].append(rating_)
    else:
        print("error")
    return plants_dict_


def update(plants_dict_, plant_, new_rarity_):
    if plant_ in plants_dict_.keys():
        plants_dict_[plant_]["rarity"] = new_rarity_
    else:
        print("error")
    return plants_dict_


def reset(plants_dict_, plant_):
    if plant_ in plants_dict_.keys():
        plants_dict_[plant_]["rating"] = []
    else:
        print("error")
    return plants_dict_


lines = int(input())
plants_dict = {}
for line in range(lines):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant not in plants_dict.keys():
        plants_dict[plant] = {"rarity": rarity, "rating": []}
    else:
        plants_dict[plant]["rarity"] += rarity

command = input().split(": ")

while command[0] != "Exhibition":
    commands = command[1].split(" - ")
    if command[0] == "Rate":
        plant = commands[0]
        rating = int(commands[1])
        plants_dict = rate(plants_dict, plant, rating)
    elif command[0] == "Update":
        plant = commands[0]
        new_rarity = int(commands[1])
        plants_dict = update(plants_dict, plant, new_rarity)
    elif command[0] == "Reset":
        plant = commands[0]
        plants_dict = reset(plants_dict, plant)

    command = input().split(": ")

print("Plants for the exhibition:")
for key in plants_dict.keys():
    if len(plants_dict[key]['rating']) > 0:
        rating = sum(plants_dict[key]['rating']) / len(plants_dict[key]['rating'])
    else:
        rating = 0
    print(f"- {key}; Rarity: {plants_dict[key]['rarity']}; Rating: {rating:.2f}")
