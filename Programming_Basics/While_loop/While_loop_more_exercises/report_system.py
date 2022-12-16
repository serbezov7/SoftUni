needed_sum = int(input())
current_sum = 0
loop = 0
pay_by_card = 0
pay_cash = 0
transactions_by_card = 0
transactions_cash = 0
is_sum_ok = False

command = input()
while command != "End":
    command = int(command)
    loop += 1
    if loop % 2 == 0:
        if command >= 10:
            pay_by_card += command
            transactions_by_card += 1
            current_sum += command
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if command <= 100:
            pay_cash += command
            transactions_cash += 1
            current_sum += command
            print("Product sold!")
        else:
            print("Error in transaction!")
    if current_sum >= needed_sum:
        is_sum_ok = True
        break
    command = input()

if is_sum_ok:
    average_cash = pay_cash / transactions_cash
    average_card = pay_by_card / transactions_by_card
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
if command == "End":
    print("Failed to collect required money for charity.")
