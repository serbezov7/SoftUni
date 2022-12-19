mens = int(input())
women = int(input())
tables = int(input())
count_tables = 0
is_tables_full = False

for i in range(1, mens + 1):
    for j in range(1, women + 1):
        print(f"({i} <-> {j})", end=" ")
        count_tables += 1
        if count_tables == tables:
            is_tables_full = True
            break
    if is_tables_full:
        break