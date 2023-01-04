count_one_leva = int(input())
count_two_leva = int(input())
count_five_leva = int(input())
number = int(input())

for i in range(count_one_leva + 1):
    for j in range(count_two_leva + 1):
        for k in range(count_five_leva + 1):
            if (i * 1) + (j * 2) + (k * 5) == number:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {number} lv.")