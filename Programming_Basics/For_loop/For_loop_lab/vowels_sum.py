text = input()
sum = 0

for letters in text:
    if letters == "a":
        sum += 1
    elif letters == "e":
        sum += 2
    elif letters == "i":
        sum += 3
    elif letters == "o":
        sum += 4
    elif letters == "u":
        sum += 5
print(sum)