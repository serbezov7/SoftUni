import re

text = input()
pattern = r"#(([A-Za-z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#)|(\|([A-Za-z\s]+?)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|)"
result = re.finditer(pattern, text)
total_calories = 0
foods = []
dates = []
calories_list = []
for match in result:
    if "#" in match.group():
        strip = match.group().strip("#")
        food, data, calories = strip.split("#")
        total_calories += int(calories)
        foods.append(food)
        dates.append(data)
        calories_list.append(calories)
    elif "|" in match.group():
        strip = match.group().strip("|")
        food, data, calories = strip.split("|")
        total_calories += int(calories)
        foods.append(food)
        dates.append(data)
        calories_list.append(calories)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for index in range(len(foods)):
    print(f"Item: {foods[index]}, Best before: {dates[index]}, Nutrition: {calories_list[index]}")
