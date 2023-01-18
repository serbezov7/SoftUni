food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
weight_in_grams = float(input()) * 1000
flag = False

for day in range(1, 31):
    food_in_grams -= 300
    if day % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if day % 3 == 0:
        cover_in_grams -= weight_in_grams / 3
    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        flag = True
if not flag:
    print(f"Everything is fine! Puppy is happy! Food: {(food_in_grams / 1000):.2f}, Hay: {(hay_in_grams / 1000):.2f},\
 Cover: {(cover_in_grams / 1000):.2f}.")
else:
    print("Merry must go to the pet store!")
