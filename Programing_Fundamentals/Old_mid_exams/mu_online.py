def potion(health_, number_):
    initial_health = health_
    heel_amount = int(number_)
    health_ += heel_amount
    if health_ > 100:
        health_ = 100
        difference = 100 - initial_health
        print(f"You healed for {difference} hp.")
    else:
        print(f"You healed for {heel_amount} hp.")
    print(f"Current health: {health_} hp.")
    return health_


def chest(bitcoins_, number_):
    amount = int(number_)
    bitcoins_ += amount
    print(f"You found {amount} bitcoins.")
    return bitcoins_


def fight(health_, attack):
    health_ -= int(attack)
    if health_ > 0:
        print(f"You slayed {command}.")
    else:
        print(f"You died! Killed by {command}.")
        print(f"Best room: {room_count}")
    return health_


rooms = input().split("|")
health = 100
bitcoins = 0
room_count = 1
flag = False
for room in rooms:
    command, number = room.split()
    if command == "potion":
        health = potion(health, number)
    elif command == "chest":
        bitcoins = chest(bitcoins, number)
    else:
        health = fight(health, number)
        if health <= 0:
            flag = True
            break
    room_count += 1
if not flag:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
