count_groups = int(input())
musala_climbers = 0
monblanc_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
all_climbers = 0

for groups in range(count_groups):
    count_people = int(input())
    all_climbers += count_people
    if count_people <= 5:
        musala_climbers += count_people
    elif count_people <= 12:
        monblanc_climbers += count_people
    elif count_people <= 25:
        kilimandjaro_climbers += count_people
    elif count_people <= 40:
        k2_climbers += count_people
    else:
        everest_climbers += count_people

percent_musala = musala_climbers / all_climbers * 100
percent_monblanc = monblanc_climbers / all_climbers * 100
percent_kilimandjaro = kilimandjaro_climbers / all_climbers * 100
percent_k2 = k2_climbers / all_climbers * 100
percent_everest = everest_climbers / all_climbers * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblanc:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")