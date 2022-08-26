chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_veg_menu = veg_menu * 8.15
dessert = (price_chicken_menu + price_fish_menu+price_veg_menu) * 0.20

price_order = price_chicken_menu + price_fish_menu + price_veg_menu + dessert + 2.50
print(price_order)
