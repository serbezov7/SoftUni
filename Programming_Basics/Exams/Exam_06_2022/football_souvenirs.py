team_name = input()
kind_souvenirs = input()
count_souvenirs = int(input())
price = 0
is_team_valid = True
is_kind_souvenirs = True

if kind_souvenirs == "flags":
    if team_name == "Argentina":
        price = count_souvenirs * 3.25
    elif team_name == "Brazil":
        price = count_souvenirs * 4.20
    elif team_name == "Croatia":
        price = count_souvenirs * 2.75
    elif team_name == "Denmark":
        price = count_souvenirs * 3.10
    else:
        print("Invalid country!")
        is_team_valid = False

elif kind_souvenirs == "caps":
    if team_name == "Argentina":
        price = count_souvenirs * 7.20
    elif team_name == "Brazil":
        price = count_souvenirs * 8.50
    elif team_name == "Croatia":
        price = count_souvenirs * 6.90
    elif team_name == "Denmark":
        price = count_souvenirs * 6.50
    else:
        print("Invalid country!")
        is_team_valid = False
elif kind_souvenirs == "posters":
    if team_name == "Argentina":
        price = count_souvenirs * 5.10
    elif team_name == "Brazil":
        price = count_souvenirs * 5.35
    elif team_name == "Croatia":
        price = count_souvenirs * 4.95
    elif team_name == "Denmark":
        price = count_souvenirs * 4.80
    else:
        print("Invalid country!")
        is_team_valid = False
elif kind_souvenirs == "stickers":
    if team_name == "Argentina":
        price = count_souvenirs * 1.25
    elif team_name == "Brazil":
        price = count_souvenirs * 1.20
    elif team_name == "Croatia":
        price = count_souvenirs * 1.10
    elif team_name == "Denmark":
        price = count_souvenirs * 0.90
    else:
        print("Invalid country!")
        is_team_valid = False
else:
    print("Invalid stock!")
    is_kind_souvenirs = False

if is_team_valid and is_kind_souvenirs:
    print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")



# team_name = input()
# kind_souvenirs = input()
# count_souvenirs = int(input())
# price = 0
#
# if kind_souvenirs == "flags":
#     if team_name == "Argentina":
#         price = count_souvenirs * 3.25
#     elif team_name == "Brazil":
#         price = count_souvenirs * 4.20
#     elif team_name == "Croatia":
#         price = count_souvenirs * 2.75
#     elif team_name == "Denmark":
#         price = count_souvenirs * 3.10
#     else:
#         print("Invalid country!")
# elif kind_souvenirs == "caps":
#     if team_name == "Argentina":
#         price = count_souvenirs * 7.20
#     elif team_name == "Brazil":
#         price = count_souvenirs * 8.50
#     elif team_name == "Croatia":
#         price = count_souvenirs * 6.90
#     elif team_name == "Denmark":
#         price = count_souvenirs * 6.50
#     else:
#         print("Invalid country!")
# elif kind_souvenirs == "posters":
#     if team_name == "Argentina":
#         price = count_souvenirs * 5.10
#     elif team_name == "Brazil":
#         price = count_souvenirs * 5.35
#     elif team_name == "Croatia":
#         price = count_souvenirs * 4.95
#     elif team_name == "Denmark":
#         price = count_souvenirs * 4.80
#     else:
#         print("Invalid country!")
# elif kind_souvenirs == "stickers":
#     if team_name == "Argentina":
#         price = count_souvenirs * 1.25
#     elif team_name == "Brazil":
#         price = count_souvenirs * 1.20
#     elif team_name == "Croatia":
#         price = count_souvenirs * 1.10
#     elif team_name == "Denmark":
#         price = count_souvenirs * 0.90
#     else:
#         print("Invalid country!")
# else:
#     print("Invalid stock!")
#
# if (team_name == "Argentina" or team_name == "Brazil" or team_name == "Croatia" or team_name == "Denmark") and \
#         (kind_souvenirs == "flags" or kind_souvenirs == "caps" or kind_souvenirs == "posters" or
#             kind_souvenirs == "stickers"):
#     print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")




# team_name = input()
# kind_souvenirs = input()
# count_souvenirs = int(input())
# price = 0
#
# if kind_souvenirs == "flags":
#     if team_name == "Argentina":
#         price = count_souvenirs * 3.25
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Brazil":
#         price = count_souvenirs * 4.20
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Croatia":
#         price = count_souvenirs * 2.75
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Denmark":
#         price = count_souvenirs * 3.10
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     else:
#         print("Invalid country!")
# elif kind_souvenirs == "caps":
#     if team_name == "Argentina":
#         price = count_souvenirs * 7.20
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Brazil":
#         price = count_souvenirs * 8.50
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Croatia":
#         price = count_souvenirs * 6.90
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Denmark":
#         price = count_souvenirs * 6.50
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     else:
#         print("Invalid country!")
# elif kind_souvenirs == "posters":
#     if team_name == "Argentina":
#         price = count_souvenirs * 5.10
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Brazil":
#         price = count_souvenirs * 5.35
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Croatia":
#         price = count_souvenirs * 4.95
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Denmark":
#         price = count_souvenirs * 4.80
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     else:
#         print("Invalid country!")
# elif kind_souvenirs == "stickers":
#     if team_name == "Argentina":
#         price = count_souvenirs * 1.25
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Brazil":
#         price = count_souvenirs * 1.20
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Croatia":
#         price = count_souvenirs * 1.10
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     elif team_name == "Denmark":
#         price = count_souvenirs * 0.90
#         print(f"Pepi bought {count_souvenirs} {kind_souvenirs} of {team_name} for {price:.2f} lv.")
#     else:
#         print("Invalid country!")
# else:
#     print("Invalid stock!")