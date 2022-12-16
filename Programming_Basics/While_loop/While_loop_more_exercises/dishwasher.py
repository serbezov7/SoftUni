bottle_washer = int(input())
washer_in_ml = bottle_washer * 750
counter = 0
plates_washer = 5
pots_washer = 15
clean_plates = 0
clean_pots = 0
washer_empty = False

command = input()
while command != "End":
    command = int(command)
    counter += 1
    if counter % 3 == 0:
        washer_in_ml = washer_in_ml - command * pots_washer
        clean_pots += command
    else:
        washer_in_ml = washer_in_ml - command * plates_washer
        clean_plates += command
    if washer_in_ml < 0:
        washer_empty = True
        break
    command = input()

if washer_empty:
    print(f"Not enough detergent, {abs(washer_in_ml)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{clean_plates} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {washer_in_ml} ml.")