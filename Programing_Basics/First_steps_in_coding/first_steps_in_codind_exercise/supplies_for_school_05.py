pen_pack = int(input())
marker_pack = int(input())
cleaning_fluid = int(input())
percent_discount = int(input())

price_pen_pack = pen_pack * 5.80
price_marker_pack = marker_pack * 7.20
price_cleaning_fluid = cleaning_fluid * 1.20

price_without_discount = price_pen_pack + price_marker_pack + price_cleaning_fluid
discount = (price_without_discount * percent_discount / 100)
price_with_discount = price_without_discount - discount

print(price_with_discount)
