eggs_size = input()
eggs_color = input()
count_batches = int(input())
price = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        price = 16
    elif eggs_color == "Green":
        price = 12
    else:
        price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = 13
    elif eggs_color == "Green":
        price = 9
    else:
        price = 7
else:
    if eggs_color == "Red":
        price = 9
    elif eggs_color == "Green":
        price = 8
    else:
        price = 5
total_price = price * count_batches * 0.65
print(f"{total_price:.2f} leva.")
