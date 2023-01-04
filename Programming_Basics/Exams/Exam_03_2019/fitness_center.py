count_visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
work_out = 0
protein = 0

for group in range(count_visitors):
    activity = input()
    if activity == "Back":
        back += 1
        work_out += 1
    elif activity == "Chest":
        chest += 1
        work_out += 1
    elif activity == "Legs":
        legs += 1
        work_out += 1
    elif activity == "Abs":
        abs += 1
        work_out += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein += 1
for_training = work_out / count_visitors * 100
for_protein = protein / count_visitors * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{for_training:.2f}% - work out")
print(f"{for_protein:.2f}% - protein")