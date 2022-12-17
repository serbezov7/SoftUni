destination = input()

while destination != "End":
    needed_money = float(input())
    saved_money = 0
    while saved_money < needed_money:
        current_money = float(input())
        saved_money += current_money
        if saved_money >= needed_money:
            print(f"Going to {destination}!")
    destination = input()
