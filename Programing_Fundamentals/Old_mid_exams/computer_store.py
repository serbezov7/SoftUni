command = input()
price_without_taxes = 0

while command != "special" and command != "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_taxes += current_price
    command = input()

price_with_taxes = price_without_taxes * 1.20
taxes = price_with_taxes - price_without_taxes
if command == "special":
    price_with_taxes *= 0.90
if price_with_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_taxes:.2f}$\n\
Taxes: {taxes:.2f}$\n\
-----------\n\
Total price: {price_with_taxes:.2f}$")