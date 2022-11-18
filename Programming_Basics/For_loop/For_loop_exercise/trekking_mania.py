groups_count = int(input())

musala_count = 0
montblanc_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0
all_people = 0

for numbers in range(groups_count):
    count_people = int(input())
    all_people += count_people
    if count_people <= 5:
        musala_count += count_people
    elif count_people <= 12:
        montblanc_count += count_people
    elif count_people <= 25:
        kilimandjaro_count += count_people
    elif count_people <= 40:
        k2_count += count_people
    else:
        everest_count += count_people

musala_percent = musala_count / all_people * 100
print(f"{musala_percent:.2f}%")
moncblant_percent = montblanc_count / all_people * 100
print(f"{moncblant_percent:.2f}%")
kilimandjaro_percent = kilimandjaro_count / all_people * 100
print(f"{kilimandjaro_percent:.2f}%")
k2_percent = k2_count / all_people * 100
print(f"{k2_percent:.2f}%")
everest_count_percent = everest_count / all_people * 100
print(f"{everest_count_percent:.2f}%")