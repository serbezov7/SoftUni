def add_city(cities_dict_):
    command_ = input().split("||")
    while command_[0] != "Sail":
        city_ = command_[0]
        population_ = int(command_[1])
        gold_ = int(command_[2])
        if city_ not in cities_dict_.keys():
            cities_dict_[city_] = [population_, gold_]
        else:
            cities_dict_[city_][0] += population_
            cities_dict_[city_][1] += gold_

        command_ = input().split("||")
    return cities_dict_


def plunder(cities_dict_, town_, people_, gold_):
    print(f"{town_} plundered! {gold_} gold stolen, {people_} citizens killed.")
    cities_dict_[town_][0] -= people_
    cities_dict_[town_][1] -= gold_
    if cities_dict_[town_][0] == 0 or cities_dict_[town_][1] == 0:
        del cities_dict_[town_]
        print(f"{town_} has been wiped off the map!")
    return cities_dict_


def prosper(cities_dict_, town_, gold_):
    if gold_ < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities_dict_[town_][1] += gold_
        print(f"{gold_} gold added to the city treasury. {town_} now has {cities_dict_[town_][1]} gold.")
    return cities_dict_


cities_dict = {}
cities_dict = add_city(cities_dict)

command = input().split("=>")

while command[0] != "End":
    town = command[1]
    if command[0] == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        cities_dict = plunder(cities_dict, town, people, gold)
    elif command[0] == "Prosper":
        gold = int(command[2])
        cities_dict = prosper(cities_dict, town, gold)

    command = input().split("=>")
if len(cities_dict.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:")
    for city in cities_dict.keys():
        print(f"{city} -> Population: {cities_dict[city][0]} citizens, Gold: {cities_dict[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
