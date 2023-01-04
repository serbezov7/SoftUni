fruit = input()
package = input()
count_packages = int(input())
price = 0
if package == "small":
    if fruit == "Watermelon":
        price = 56 * 2
    elif fruit == "Mango":
        price = 36.66 * 2
    elif fruit == "Pineapple":
        price = 42.10 * 2
    else:
        price = 20 * 2
else:
    if fruit == "Watermelon":
        price = 28.70 * 5
    elif fruit == "Mango":
        price = 19.60 * 5
    elif fruit == "Pineapple":
        price = 24.80 * 5
    else:
        price = 15.20 * 5

total_price = price * count_packages
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5
print(f"{total_price:.2f} lv.")