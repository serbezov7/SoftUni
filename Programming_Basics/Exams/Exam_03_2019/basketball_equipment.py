annual_tax = int(input())
shoes = annual_tax * 0.6
sport_suit = shoes * 0.8
ball = sport_suit / 4
accessories = ball / 5
all = shoes + sport_suit + ball + accessories + annual_tax
print(f"{all:.2f}")