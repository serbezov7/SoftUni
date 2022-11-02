chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
rest_day = input()
price_chrysanthemums = 0
price_roses = 0
price_tulips = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemums = chrysanthemums * 2
    price_roses = roses * 4.10
    price_tulips = tulips * 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = chrysanthemums * 3.75
    price_roses = roses * 4.50
    price_tulips = tulips * 4.15
total_price = price_chrysanthemums + price_roses + price_tulips
total_flowers = chrysanthemums + roses + tulips
if rest_day == "Y":
    total_price = total_price * 1.15
if season == "Spring" and tulips > 7:
    total_price = total_price * 0.95
elif season == "Winter" and roses >= 10:
    total_price = total_price * 0.9
if total_flowers > 20:
    total_price = total_price * 0.80
final_price = total_price + 2
print(f"{final_price:.2f}")
