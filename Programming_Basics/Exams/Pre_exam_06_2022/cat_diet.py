percent_fat = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())
total_fat = total_calories * percent_fat / 9
total_proteins = total_calories * percent_proteins / 4
total_carbohydrates = total_calories * percent_carbohydrates / 4
food_weight = total_fat + total_proteins + total_carbohydrates
calories_per_gram = total_calories / food_weight
calories_per_gram_without_water = calories_per_gram * (100 - percent_water)
print(f"{calories_per_gram_without_water:.4f}")