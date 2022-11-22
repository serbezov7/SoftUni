game_moves = int(input())
points = 0
sum_0_9 = 0
sum_10_19 = 0
sum_20_29 = 0
sum_30_39 = 0
sum_40_50 = 0
sum_invalid_numbers = 0

for numbers in range(game_moves):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.2
        sum_0_9 += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        sum_10_19 += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        sum_20_29 += 1
    elif 30 <= number <= 39:
        points += 50
        sum_30_39 += 1
    elif 40 <= number <= 50:
        points += 100
        sum_40_50 += 1
    else:
        points /= 2
        sum_invalid_numbers += 1

percent_0_9 = sum_0_9 / game_moves * 100
percent_10_19 = sum_10_19 / game_moves * 100
percent_20_29 = sum_20_29 / game_moves * 100
percent_30_39 = sum_30_39 / game_moves * 100
percent_40_50 = sum_40_50 / game_moves * 100
percent_invalid = sum_invalid_numbers / game_moves * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_0_9:.2f}%")
print(f"From 10 to 19: {percent_10_19:.2f}%")
print(f"From 20 to 29: {percent_20_29:.2f}%")
print(f"From 30 to 39: {percent_30_39:.2f}%")
print(f"From 40 to 50: {percent_40_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
