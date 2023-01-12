import re
pattern = r">{2}([]A-Za-z]+)<{2}(\d+(\.\d+)*)!(\d+)"
command = input()
furniture = []
total_money = 0
while command != "Purchase":
    result = re.findall(pattern, command)
    if result:
        furniture.append(result[0][0])
        total_money += float(result[0][1]) * int(result[0][3])

    command = input()
print("Bought furniture:")
for match in furniture:
    print(match)
print(f"Total money spend: {total_money:.2f}")