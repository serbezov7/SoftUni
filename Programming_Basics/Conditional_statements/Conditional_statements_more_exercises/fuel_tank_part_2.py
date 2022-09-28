fuel_type = input()
fuel_liters = float(input())
discount_card = input()
discount_gas = 0.08
discount_gasoline = 0.18
discount_diesel = 0.12
price_gas = 0.93
price_gasoline = 2.22
price_diesel = 2.33

total_fuel_price = 0
if fuel_type == "Gas":
    if discount_card == "Yes":
        total_fuel_price = (fuel_liters * price_gas) - (fuel_liters * discount_gas)
    else:
        total_fuel_price = fuel_liters * price_gas
elif fuel_type == "Gasoline":
    if discount_card == "Yes":
        total_fuel_price = (fuel_liters * price_gasoline) - (fuel_liters * discount_gasoline)
    else:
        total_fuel_price = fuel_liters * price_gasoline
else:
    if discount_card == "Yes":
        total_fuel_price = (fuel_liters * price_diesel) - (fuel_liters * discount_diesel)
    else:
        total_fuel_price = fuel_liters * price_diesel

if 20 <= fuel_liters <= 25:
    total_fuel_price = total_fuel_price * 0.92
elif fuel_liters > 25:
    total_fuel_price = total_fuel_price * 0.9

print(f"{total_fuel_price:.2f} lv.")



# if fuel_type == "Gas" and discount_card == "Yes":
#     total_fuel_price = fuel_liters * 0.85
# elif fuel_liters == "Gas" and discount_card == "No":
#     total_fuel_price = fuel_liters * 0.93
# elif fuel_type == "Gasoline" and discount_card == "Yes":
#     total_fuel_price = fuel_liters * 2.07
# elif fuel_type == "Gasoline" and discount_card == "No":
#     total_fuel_price = fuel_liters * 2.22
# elif fuel_type == "Diesel" and discount_card == "Yes":
#     total_fuel_price = fuel_liters * 2.21
# elif fuel_type == "Diesel" and discount_card == "No":
#     total_fuel_price = fuel_liters * 2.33
#
# if 20 <= fuel_liters <= 25:
#     total_fuel_price = total_fuel_price * 0.92
# elif fuel_liters > 25:
#     total_fuel_price = total_fuel_price * 0.9
# print(f"{total_fuel_price:.2f} lv.")


