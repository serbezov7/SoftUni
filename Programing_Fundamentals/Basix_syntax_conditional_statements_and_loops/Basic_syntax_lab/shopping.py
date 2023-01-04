budget = int(input())

command = input()
while command != "End":
    current_price = int(command)
    budget -= current_price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")