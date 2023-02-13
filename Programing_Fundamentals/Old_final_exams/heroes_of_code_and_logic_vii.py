def create_hero(heroes_dict_, number_of_heroes_):
    for hero in range(number_of_heroes_):
        data = input().split()
        hero_name_ = data[0]
        hit_points_ = int(data[1])
        mana_points_ = int(data[2])
        heroes_dict_[hero_name_] = [hit_points_, mana_points_]

    return heroes_dict_


def cast_spell(heroes_dict_, hero_name_, needed_mp_, spell_name_):
    if heroes_dict_[hero_name_][1] >= needed_mp_:
        heroes_dict_[hero_name_][1] -= needed_mp_
        mana_points = heroes_dict_[hero_name_][1]
        print(f"{hero_name_} has successfully cast {spell_name_} and now has {mana_points} MP!")
    else:
        print(f"{hero_name_} does not have enough MP to cast {spell_name_}!")
    return heroes_dict_


def take_damage(heroes_dict_, hero_name_, damage_, attacker_):
    heroes_dict_[hero_name_][0] -= damage_
    current_hp = heroes_dict_[hero_name_][0]
    if heroes_dict_[hero_name_][0] > 0:
        print(f"{hero_name_} was hit for {damage_} HP by {attacker_} and now has {current_hp} HP left!")
    else:
        del heroes_dict_[hero_name_]
        print(f"{hero_name_} has been killed by {attacker_}!")
    return heroes_dict_


def recharge(heroes_dict_, hero_name_, amount_):
    initial_mp = heroes_dict_[hero_name_][1]
    heroes_dict_[hero_name_][1] += amount_
    if heroes_dict_[hero_name_][1] > 200:
        heroes_dict_[hero_name_][1] = 200
        difference = 200 - initial_mp
        print(f"{hero_name_} recharged for {difference} MP!")
    else:
        print(f"{hero_name_} recharged for {amount_} MP!")
    return heroes_dict_


def heal(heroes_dict_, hero_name_, amount_):
    initial_hp = heroes_dict_[hero_name_][0]
    heroes_dict_[hero_name_][0] += amount_
    if heroes_dict_[hero_name_][0] > 100:
        heroes_dict_[hero_name_][0] = 100
        difference = 100 - initial_hp
        print(f"{hero_name_} healed for {difference} HP!")

    else:
        print(f"{hero_name_} healed for {amount_} HP!")
    return heroes_dict_


number_of_heroes = int(input())
heroes_dict = {}
heroes_dict = create_hero(heroes_dict, number_of_heroes)

command = input().split(" - ")

while command[0] != "End":
    hero_name = command[1]
    if command[0] == "CastSpell":
        needed_mp = int(command[2])
        spell_name = command[3]
        heroes_dict = cast_spell(heroes_dict, hero_name, needed_mp, spell_name)
    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes_dict = take_damage(heroes_dict, hero_name, damage, attacker)
    elif command[0] == "Recharge":
        amount = int(command[2])
        heroes_dict = recharge(heroes_dict, hero_name, amount)
    elif command[0] == "Heal":
        amount = int(command[2])
        heroes_dict = heal(heroes_dict, hero_name, amount)

    command = input().split(" - ")

for hero in heroes_dict.keys():
    print(f"{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}")
