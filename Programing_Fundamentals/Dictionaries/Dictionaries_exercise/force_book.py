command = input()
force_dict = {}

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        is_user_found = False
        for user in force_dict.values():
            if force_user in user:
                is_user_found = True
        if not is_user_found:
            if force_side not in force_dict.keys():
                force_dict[force_side] = [force_user]
            else:
                force_dict[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for side, user in force_dict.items():
            if force_user in user:
                index = force_dict[side].index(force_user)
                del force_dict[side][index]

        if force_side in force_dict.keys():
            force_dict[force_side].append(force_user)
        else:
            force_dict[force_side] = [force_user]
        print(f"{force_user} joins the {force_side} side!")

    command = input()
for side in force_dict.keys():
    if len(force_dict[side]) > 0:
        print(f"Side: {side}, Members: {len(force_dict[side])}")
        for user in force_dict[side]:
            print(f"! {user}")