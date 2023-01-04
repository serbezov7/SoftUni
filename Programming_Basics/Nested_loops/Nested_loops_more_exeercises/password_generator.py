n = int(input())
l = int(input())

for i in range(1, n):
    for j in range(1, n):
        for k in range(97, 97 + l):
            for m in range(97, 97 + l):
                for o in range(1, n + 1):
                    if o > i and o > j:
                        print(f"{i}{j}{chr(k)}{chr(m)}{o}", end=" ")

