reservations_set = set()
for _ in range(int(input())):
    res_number = input()
    reservations_set.add(res_number)
while True:
    command = input()
    if command == "END":
        break
    if command in reservations_set:
        reservations_set.remove(command)

print(len(reservations_set))
for guest in sorted(reservations_set):
    print(guest)
    