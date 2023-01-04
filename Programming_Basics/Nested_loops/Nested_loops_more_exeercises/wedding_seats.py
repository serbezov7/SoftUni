last_sector = input()
count_rows_first_sector = int(input())
count_seats_odd_row = int(input())
seats = 0
for i in range(65, ord(last_sector) + 1):
    for j in range(1, count_rows_first_sector + 1):
        if j % 2 != 0:
            for k in range(ord("a"), ord("a") + count_seats_odd_row):
                print(f"{chr(i)}{j}{chr(k)}")
                seats += 1
        elif j % 2 == 0:
            for l in range(ord("a"), ord("a") + count_seats_odd_row + 2):
                print(f"{chr(i)}{j}{chr(l)}")
                seats += 1
    count_rows_first_sector += 1
print(seats)