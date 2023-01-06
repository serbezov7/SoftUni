money = list(map(int, input().split(", ")))
beggars = int(input())

total_sums = []
beggars_count = 0
while beggars_count < beggars:
    sum_current_beggar = 0
    for current_beggar in range(beggars_count, len(money), beggars):
        sum_current_beggar += money[current_beggar]
    total_sums.append(sum_current_beggar)

    beggars_count += 1
print(total_sums)
