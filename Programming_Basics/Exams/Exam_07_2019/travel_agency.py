city = input()
package = input()
vip_discount = input()
days_stay = int(input())
price_for_day = 0
total_price = 0

if days_stay < 1:
    print("Days must be positive number!")
else:
    if city == "Bansko" or city == "Borovets":
        if package == "withEquipment":
            price_for_day = 100
            if vip_discount == "yes":
                price_for_day *= 0.9
            if days_stay > 7:
                total_price = price_for_day * (days_stay - 1)
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
            else:
                total_price = price_for_day * days_stay
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
        elif package == "noEquipment":
            price_for_day = 80
            if vip_discount == "yes":
                price_for_day *= 0.95
            if days_stay > 7:
                total_price = price_for_day * (days_stay - 1)
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
            else:
                total_price = price_for_day * days_stay
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")
    elif city == "Varna" or city == "Burgas":
        if package == "withBreakfast":
            price_for_day = 130
            if vip_discount == "yes":
                price_for_day *= 0.88
            if days_stay > 7:
                total_price = price_for_day * (days_stay - 1)
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
            else:
                total_price = price_for_day * days_stay
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
        elif package == "noBreakfast":
            price_for_day = 100
            if vip_discount == "yes":
                price_for_day *= 0.93
            if days_stay > 7:
                total_price = price_for_day * (days_stay - 1)
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
            else:
                total_price = price_for_day * days_stay
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")