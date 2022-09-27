from math import floor,ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

total_price = (magnolias * 3.25) + (hyacinths * 4) + (roses * 3.50) + (cactuses * 8)
total_price_after_taxes = total_price * 0.95
difference = abs(total_price_after_taxes - gift_price)

if gift_price <= total_price_after_taxes:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")