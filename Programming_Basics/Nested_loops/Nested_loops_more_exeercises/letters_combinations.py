first_letter = input()
second_letter = input()
third_letter = input()
count = 0
for i in range(ord(first_letter), ord(second_letter) + 1):
    for j in range(ord(first_letter), ord(second_letter) + 1):
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if chr(i) == third_letter or chr(j) == third_letter or chr(k) == third_letter:
                continue
            else:
                count += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
print(count)

