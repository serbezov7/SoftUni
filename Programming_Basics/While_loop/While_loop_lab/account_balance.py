command = input()
total_sum = 0
while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid operation!")
        break
    total_sum += current_sum
    print(f"Increase: {current_sum:.2f}")
    command = input()

print(f"Total: {total_sum:.2f}")